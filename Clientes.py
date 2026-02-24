import time
import threading

class Cliente(threading.Thread): #Clase hija de threading.Thread
    def __init__(self,id,banco):
        super().__init__() #Llamando al constructor de la clase Padre
        self.id_cliente=id
        self.banco=banco
        self.start() # Con esta linea iniciamos el hilo al construirlo, se ejecuta run()

    def run(self):
        print('Cliente llegó a hacer una transacción...')
        time.sleep(0.01)
        self.banco.accion_cliente()
