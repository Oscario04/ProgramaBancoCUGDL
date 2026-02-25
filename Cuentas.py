import threading


class Cuenta:

    def __init__(self, id_cuenta, saldo=1000):
        self.id_cuenta = id_cuenta
        self.saldo = saldo
        self.lock_cuenta = threading.RLock()

    def retirar(self, monto):
        with self.lock_cuenta:
            if monto <= self.saldo:
                self.saldo -= monto

    def depositar(self, monto):
        with self.lock_cuenta:
            self.saldo += monto

    def __repr__(self):
        return f"Cuenta {self.id_cuenta} | Saldo: {self.saldo}"