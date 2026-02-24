"""
Este programa es el principal.

Estructura del programa:
1. Importar las librerias y los subprogramas necesarios
2. Definir las variables necesarias para la ejecución del programa principal
3. Instanciamos el objeto banco, con los parametros necesarios
4. Creamos (instanciamos) los hilos Clientes (productor/consumidor) y Cajeros (consumidor/productor)
5. Iniciamos los hilos (.start()) y hacemos un .join para esperar a que terminen
6. Cerramos el banco y terminamos programa
"""
# 1. Importamos librerias y subprogramas #####
import time
import os # Libreria para limpiar la terminal de python
from Banco import Banco #from (nombre del programa) y import (nombre de la clase)
from Clientes import Cliente
from Cajeros import Cajero
# Para limpiar la terminal a; ejecutar
os.system('cls')
#####

# 2. Definamos las variables del programa. Las deberia de poder manipular el usuario
nombre_banco='Baniorte'
caja_fuerte=1000000
num_cajeros=3
num_clientes=8

# 3. Instanciamos el objeto banco con sus parametros de entrada
banco=Banco(nombre_banco,caja_fuerte,num_clientes) #Creamos el objeto banco

# 4. Creamos los hilos clientes y cajeros
# Cajeros
cajeros=[Cajero(i,banco) for i in range(num_cajeros)]
# Clientes
clientes=[Cliente(i,banco) for i in range(num_clientes)]

# Vamos a hacer un join para que terminen de hacer las transacciones
for i in range(len(clientes)): #Join de clientes
    clientes[i].join()

for i,cajero in enumerate(cajeros): #Join de cajeros
    cajero.join()

#quit()
