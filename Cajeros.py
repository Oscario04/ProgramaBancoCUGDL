import threading
import time


class Cajero(threading.Thread):

    def __init__(self, id_cajero, banco):
        super().__init__()
        self.id_cajero = id_cajero
        self.banco = banco
        self.start()

    def run(self):
        print(f"Cajero {self.id_cajero} inicia operaciones.")
        time.sleep(0.05)
        self.banco.accion_cajero()