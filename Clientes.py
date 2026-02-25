import threading
import time


class Cliente(threading.Thread):

    def __init__(self, id_cliente, banco):
        super().__init__()
        self.id_cliente = id_cliente
        self.banco = banco
        self.start()

    def run(self):
        print(f"Cliente {self.id_cliente} llegó al banco.")
        time.sleep(0.05)
        self.banco.espera_cliente(self.id_cliente)