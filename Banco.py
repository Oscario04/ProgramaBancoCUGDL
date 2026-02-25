import random
import threading
import time
from Cuentas import Cuenta
from Transacciones import Transaccion


class Banco:

    def __init__(self, nombre, caja_fuerte, num_cuentas):
        self.nombre = nombre
        self.caja_fuerte = caja_fuerte
        self.historial_transacciones = []

        self.lock = threading.Lock()              # Protege caja fuerte e historial
        self.timbre = threading.Condition()      # Controla fila

        self.cuentas = [
            Cuenta(i, random.uniform(200, 10000))
            for i in range(num_cuentas)
        ]

        self.fila_solicitudes = []
        self.capacidad_fila = 4
        self.clientes_activos = 0
        self.tiempo_espera = 0.2

    # ===============================
    # CLIENTE GENERA SOLICITUD
    # ===============================
    def espera_cliente(self, id_cliente):

        with self.timbre:
            self.clientes_activos += 1
            print(f"Cliente {id_cliente} esperando en fila...")

            while len(self.fila_solicitudes) >= self.capacidad_fila:
                print(f"Fila llena. Cliente {id_cliente} espera.")
                self.timbre.wait()

            self.fila_solicitudes.append(id_cliente)
            self.timbre.notify_all()

    # ===============================
    # CAJERO PROCESA SOLICITUD
    # ===============================
    def accion_cajero(self):

        print("Accion Cajero")

        while True:

            with self.timbre:

                # Condición de cierre segura
                if self.clientes_activos == 0 and not self.fila_solicitudes:
                    print("Cajero finaliza: no hay clientes ni fila.")
                    break

                while not self.fila_solicitudes:
                    self.timbre.wait(timeout=1)

                    if self.clientes_activos == 0 and not self.fila_solicitudes:
                        print("Cajero finaliza por inactividad.")
                        return

                id_cliente = self.fila_solicitudes.pop(0)
                self.timbre.notify_all()

            # Procesar solicitud
            self.procesar_operacion(id_cliente)

            with self.timbre:
                self.clientes_activos -= 1

            time.sleep(self.tiempo_espera)

    # ===============================
    # LÓGICA DE OPERACIONES
    # ===============================
    def procesar_operacion(self, id_cliente):

        cuenta = random.choice(self.cuentas)
        cuenta_destino = random.choice(
            [c for c in self.cuentas if c != cuenta]
        )

        accion = random.choice(["retiro", "deposito", "consulta", "transferencia"])

        if accion == "retiro":
            monto = random.uniform(50, 500)
            with self.lock:
                print(f"Cliente {id_cliente}: Solicitud de retiro en cuenta {cuenta.id_cuenta}")
                print(f"Saldo antes: {cuenta.saldo:.2f}, Monto a retirar: {monto:.2f}")
                if monto <= cuenta.saldo:
                    cuenta.retirar(monto)
                    self.caja_fuerte -= monto
                    print(f"Retiro realizado. Saldo final: {cuenta.saldo:.2f}")
                    self.registrar_tx(id_cliente, "Retiro", cuenta.id_cuenta, monto)
                else:
                    print(f"No hay suficiente saldo para retirar {monto:.2f}")

        elif accion == "deposito":
            monto = random.uniform(50, 500)
            with self.lock:
                print(f"Cliente {id_cliente}: Solicitud de depósito en cuenta {cuenta.id_cuenta}")
                print(f"Saldo antes: {cuenta.saldo:.2f}, Monto a depositar: {monto:.2f}")
                cuenta.depositar(monto)
                self.caja_fuerte += monto
                print(f"Depósito realizado. Saldo final: {cuenta.saldo:.2f}")
                self.registrar_tx(id_cliente, "Depósito", cuenta.id_cuenta, monto)

        elif accion == "consulta":
            with self.lock:
                saldo = cuenta.saldo
                print(f"Cliente {id_cliente}: Consulta de saldo en cuenta {cuenta.id_cuenta}: {saldo:.2f}")
                self.registrar_tx(id_cliente, "Consulta", cuenta.id_cuenta, saldo)

        elif accion == "transferencia":
            monto = random.uniform(50, 500)
            with self.lock:
                print(f"Cliente {id_cliente}: Solicitud de transferencia de cuenta {cuenta.id_cuenta} a cuenta {cuenta_destino.id_cuenta}")
                print(f"Saldo origen antes: {cuenta.saldo:.2f}, saldo destino antes: {cuenta_destino.saldo:.2f}, Monto: {monto:.2f}")
                if monto <= cuenta.saldo:
                    cuenta.retirar(monto)
                    cuenta_destino.depositar(monto)
                    print(f"Transferencia realizada. Saldo origen final: {cuenta.saldo:.2f}, saldo destino final: {cuenta_destino.saldo:.2f}")
                    self.registrar_tx(id_cliente, "Transferencia", cuenta_destino.id_cuenta, monto)
                else:
                    print(f"No hay suficiente saldo para transferir {monto:.2f}")

    # ===============================
    # REGISTRO DE TRANSACCIONES
    # ===============================
    def registrar_tx(self, id_cliente, tipo, cuenta_destino, monto):

        tx = Transaccion(
            len(self.historial_transacciones) + 1,
            id_cliente,
            tipo,
            cuenta_destino,
            monto
        )

        self.historial_transacciones.append(tx)