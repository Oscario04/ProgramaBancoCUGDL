class Transaccion:

    def __init__(self, id_tx, id_cliente, tipo, cuenta_destino, monto):
        self.id_transaccion = id_tx
        self.id_cliente = id_cliente
        self.tipo = tipo
        self.cuenta_destino = cuenta_destino
        self.monto = monto

    def __repr__(self):
        return f"TX {self.id_transaccion} | {self.tipo} | Cliente {self.id_cliente} | Monto {self.monto}"