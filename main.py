
import os
import platform
import random
from Banco import Banco
from Clientes import Cliente
from Cajeros import Cajero


# Limpiar consola compatible
if platform.system() == "Windows":
    os.system("cls")
else:
    os.system("clear")

# Parámetros
nombre_banco = "Baniorte"
caja_fuerte = 1_000_000
num_cajeros = 3
num_clientes = 8

# Crear banco
banco = Banco(nombre_banco, caja_fuerte, num_clientes)

# Crear cajeros
cajeros = [Cajero(i, banco) for i in range(num_cajeros)]


# Esperar clientes
clientes = [Cliente(i, banco) for i in range(num_clientes)]
for cliente in clientes:
    cliente.join()


# Esperar cajeros
for cajero in cajeros:
    cajero.join()


# Forzar mínimo de 20 transacciones
while len(banco.historial_transacciones) < 20:
    banco.procesar_operacion(random.randint(0, num_clientes-1))


print("\nBanco cerrado correctamente.")
print(f"Total transacciones: {len(banco.historial_transacciones)}")