
# ProgramaBancoCUGDL

## Descripción
ProgramaBancoCUGDL es una simulación de un sistema bancario multihilo en Python, donde clientes y cajeros interactúan con cuentas y una caja fuerte. El programa utiliza hilos para simular concurrencia y operaciones bancarias reales como depósitos, retiros y consultas de saldo.

## Estructura del proyecto

```
ProgramaBancoCUGDL/
├── Banco.py           # Lógica principal del banco, gestión de cuentas y transacciones
├── Cajeros.py         # Clase Cajero, ejecuta operaciones bancarias como hilo
├── Clientes.py        # Clase Cliente, solicita operaciones bancarias como hilo
├── Cuentas.py         # Clase Cuenta, maneja saldo y operaciones básicas
├── Transacciones.py   # Clase Transaccion, registra cada operación realizada
├── main.py            # Script principal, inicializa el banco y los hilos
├── __init__.py        # Inicialización del paquete
├── README.md          # Documentación del proyecto
├── __pycache__/       # Archivos de caché de Python
├── .venv/             # Entorno virtual de Python
```

## Descripción de las funciones principales

- **Banco**: Administra cuentas, caja fuerte y el historial de transacciones. Valida operaciones y protege recursos compartidos con locks.
- **Cuenta**: Permite depositar y retirar dinero, con validaciones de saldo y protección de concurrencia.
- **Cliente**: Hilo que simula la llegada de un cliente y solicita operaciones (retiro, depósito, consulta).
- **Cajero**: Hilo que simula la atención de solicitudes de clientes.
- **Transaccion**: Registra cada operación realizada (retiro, depósito, consulta) con detalles como monto, cuenta y cliente.
- **main.py**: Inicializa el banco, crea hilos de clientes y cajeros, y ejecuta la simulación.

## TO DO / Mejoras posibles

- [ ] Implementar una interfaz gráfica o CLI interactiva para el usuario.
- [ ] Agregar pruebas unitarias para asegurar la robustez del sistema.
- [ ] Mejorar el manejo de errores y excepciones.
- [ ] Permitir configuración dinámica de parámetros (número de clientes, cajeros, etc).
- [ ] Registrar el historial de transacciones en un archivo externo (log).
- [ ] Implementar autenticación de clientes y cajeros.
- [ ] Simular más tipos de transacciones (transferencias, pagos, etc).
- [ ] Optimizar la gestión de concurrencia y recursos compartidos.

---
Proyecto desarrollado en Python para la materia de Computación y Sistemas en CUGDL.
