"""
Este programa define una clase Cuenta con sus atributos y métodos.

Procesos internos:
1. Incremente saldo (cuando haya un depósito)
2. Reduzca el saldo (cuando hay un retiro)
"""

import time
import threading

class Cuenta():
    def __init__(self,id_cuenta,saldo=1000):
        self.saldo=saldo
        self.id_cuenta=id_cuenta
        self.productos=[]
        self.lock_cuenta=threading.RLock()

    def retirar(self,monto):
        with self.lock_cuenta:
            if monto>self.saldo:
                print('No hay suficiente dinero en la cuenta')
                pass
            elif monto==self.saldo:
                self.saldo-=monto
                print(f'Cuenta {self.id_cuenta} en ceros.')
            else:
                self.saldo-=monto #El saldo se reduce un cierto monto

    def depositar(self,monto):
        with self.lock_cuenta:
            self.saldo+=monto #El saldo se incrementa un cierto monto

    def __repr__(self): #Método interno de python para imprimir cuando haga print del objeto
        return f'Cuenta {self.id_cuenta}. Saldo final: {self.saldo}'