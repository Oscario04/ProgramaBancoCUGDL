"""
Acciones del cliente:
1. Solicitar un retiro
2. Hacer un depósito
3. Consultar saldo

Acciones del cajero:
1. Realizar un retiro a solicitud del cliente
2. Agregar dinero a una cuenta (Hacer depósito)
3. Dar información de su saldo al cliente

Cajero cunple las solicitudes del Cliente y Manipula el saldo de la Caja fuerte,
y marca el cambio en las cuentas de los usuarios.
"""     

import time
from Cuentas import Cuenta
## Importe de transacciones
import random
import threading


class Banco():
    def __init__(self,nombre,caja_fuerte,num_cuentas):
        self.historial_transacciones = []
        self.caja_fuerte = caja_fuerte
        self.nombre = nombre
        self.lock = threading.Lock() # Candado para la bóveda/caja fuerte
        # Creacion de las cuentas
        # Cada cuenta tendrá un saldo distinto a través de un número aleatorio entre 200 y 10000
        self.cuentas = [Cuenta(i, random.uniform(200, 10000)) for i in range(num_cuentas)] # Lista con objetos cuentas
        self.tiempo_espera = 5
        # Necesitamos una fila de solicitudes realizadas por los clientes
        # para ser atendidas por los cajeros
        self.fila_solicitudes = [] # No hay fila al abrir el banco
        self.capacidad_fila = 4 # Cantidad maxima de transacciones en la fila
        self.timbre = threading.Condition() # Condition variable

    
    def accion_cliente(self):
        print('Accion del Cliente')
        eleccion = random.choice([1,2,3]) # simulamos la elección aleatoria de una operación
        cuenta = random.choice(self.cuentas) # Elegir una cuenta aleatoria
        id_cliente = random.randint(1, 1000)
        with self.timbre:
            match eleccion:
                case 1:
                    print(f'Solicitud de retiro en cuenta {cuenta.id_cuenta}')
                    monto = random.uniform(50, 500)
                    with self.lock:
                        if monto > cuenta.saldo:
                            print(f'No hay suficiente dinero en la cuenta {cuenta.id_cuenta} para retirar {monto:.2f}')
                        elif monto <= 0:
                            print(f'Monto inválido para retiro en cuenta {cuenta.id_cuenta}')
                        else:
                            cuenta.retirar(monto)
                            self.caja_fuerte -= monto
                            from Transacciones import Transaccion
                            tx = Transaccion(len(self.historial_transacciones)+1, id_cliente, 'Retiro', cuenta.id_cuenta, monto)
                            self.historial_transacciones.append(tx)
                    time.sleep(self.tiempo_espera)
                case 2:
                    print(f'Solicitud de depósito en cuenta {cuenta.id_cuenta}')
                    monto = random.uniform(50, 500)
                    with self.lock:
                        if monto <= 0:
                            print(f'Monto inválido para depósito en cuenta {cuenta.id_cuenta}')
                        else:
                            cuenta.depositar(monto)
                            self.caja_fuerte += monto
                            from Transacciones import Transaccion
                            tx = Transaccion(len(self.historial_transacciones)+1, id_cliente, 'Depósito', cuenta.id_cuenta, monto)
                            self.historial_transacciones.append(tx)
                    time.sleep(self.tiempo_espera)
                case 3:
                    print(f'Solicitud de Consulta de Saldo en cuenta {cuenta.id_cuenta}')
                    with self.lock:
                        print(f'Saldo actual de la cuenta {cuenta.id_cuenta}: {cuenta.saldo}')
                        from Transacciones import Transaccion
                        tx = Transaccion(len(self.historial_transacciones)+1, id_cliente, 'Consulta', cuenta.id_cuenta, cuenta.saldo)
                        self.historial_transacciones.append(tx)
                    time.sleep(self.tiempo_espera)
        
    
    def accion_cajero(self):
        print("Accion Cajero")