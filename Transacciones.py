"""
Clase Transacciones

Atributos:
1. id_transaccion
2. Id del cliente
3. Si es deposito,retiro o consulta saldo
4. Monto
5. Numero de cuenta destino
"""
import time
class Transaccion():
    def __init__(self,id_tx,id_cliente,tipo_transaccion,cuenta_destino,monto=0):
        self.id_transaccion=id_tx
        self.id_cliente=id_cliente
        self.tipo=tipo_transaccion #Deposito, Retiro, Consulta
        self.monto=monto
        self.cuenta_destino=cuenta_destino
    
    def __repr__(self):
        return f'Transaccion {self.id_transaccion}: {self.tipo}. Monto: {self.monto}'
