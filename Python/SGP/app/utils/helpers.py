# --- Librería estándar de Python (viene con Python) ---
import os

# --- Librerías externas / de terceros (pip install ...) ---
from tabulate import tabulate

def leer_int(mensaje, minimo=None, maximo=None):
    while True:
        txt = input(mensaje).strip()

        try:
            numero = int(txt)
        except ValueError:
            print("Debes ingresar un número entero válido.")
            continue

        if minimo is not None and numero < minimo:
            print(f"Debe ser mayor o igual a {minimo}.")
            continue

        if maximo is not None and numero > maximo:
            print(f"Debe ser menor o igual a {maximo}.")
            continue

        return numero

def imprimir_tabla(datos: dict, headers: list[str] | None = None, formato: str = "grid"):
    """
    Imprime un diccionario como tabla en consola usando la librería tabulate.

    La función recibe un diccionario simple o un diccionario de diccionarios y
    lo transforma en una tabla legible para mostrar en consola.

    Parámetros
    ----------
    datos : dict
        Diccionario a mostrar. Ejemplos válidos:
        - {"Ana": 6.5, "Juan": 5.8}
        - {"Ana": {"nota": 6.5, "asistencia": 95}}
    headers : list[str] | None, opcional
        Encabezados de la tabla. Si es None, se generan automáticamente.
    formato : str, opcional
        Estilo de la tabla (por defecto "grid").
        Ejemplos: "grid", "simple", "github", "fancy_grid".

    Retorna
    -------
    None
        La función solo imprime la tabla, no retorna valores.

    Requiere
    --------
    tabulate (librería externa)
    Instalar con: python -m pip install tabulate
    """

    if not datos:
        print("No hay datos para mostrar.")
        return

    filas = []

    # Caso 1: diccionario simple
    if not isinstance(next(iter(datos.values())), dict):
        if headers is None:
            headers = ["Clave", "Valor"]

        for clave, valor in datos.items():
            filas.append([clave, valor])

    # Caso 2: diccionario de diccionarios
    else:
        columnas = list(next(iter(datos.values())).keys())

        if headers is None:
            headers = ["Clave"] + columnas

        for clave, subdic in datos.items():
            filas.append([clave] + list(subdic.values()))

    print(tabulate(filas, headers=headers, tablefmt=formato))

def pausa():
    input("\nPresiona ENTER para continuar...")


def limpiar_consola():
    os.system('cls')

def sin_datos():
    print("\n No hay productos...")

def mensaje_no_encontrado():
    print("\n Producto no encontrado...")

def mensaje_orden_exitosa():
    print("\n Orden ejecutada exitosamente...")