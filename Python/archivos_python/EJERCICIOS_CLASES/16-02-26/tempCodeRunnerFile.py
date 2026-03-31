"""
Explorador de archivos simple
Contexto:
Estás creando una herramienta que
permita a los usuarios inspeccionar
archivos locales. El objetivo es obtener
información del archivo y mostrar su
contenido de manera distinta según su
tamaño, usando buenas prácticas de
manejo de archivos en Python.

Tiempo : 50 Minutos

Consigna:
● Implementá un programa en Python que:
○ Solicite al usuario el nombre de un archivo
○ Abra el archivo en modo lectura ("r")
○ Obtenga y muestre:
■ Nombre del archivo (.name)
■ Modo de apertura (.mode)
■ Estado de cierre (.closed)
■ Tamaño en bytes usando os.stat()
○ Lea el contenido:
■ Si el archivo pesa menos de 500 bytes →
leé todo el contenido con read()
■ Si pesa más de 500 bytes → leé línea por
línea con readline()

● Asegurate de cerrar el archivo y mostrar que fue
cerrado correctamente
● Usá try/except para manejar errores si el archivo no
existe
"""

import os


def traducir_modo_apertura(modo):
    modos = {
        "r": "Lectura",
        "w": "Escritura",
    }
    if modo in modos:
        return modos[modo]

    return modo


def centrar_titulo(cadena):
    print(f"\n{cadena:^40}\n")


def cerrar_archivo(archivo):
    archivo.close()
    if archivo.closed:
        print("\nArchivo cerrado correctamente ...\n")
    else:
        print("\nHubo un problema al cerrar el archivo ...\n")


def imprimir_contenido(contenido):
    print("=" * 70)
    print(contenido)
    print("=" * 70)


nombre_archivo = input("Ingrese nombre del archivo: ")

try:

    archivo = open(
        f"archivos_python/EJERCICIOS_CLASES/16-02-26/{nombre_archivo.strip()}.txt",
        "r",
        encoding="utf-8",
    )

    centrar_titulo("<< Información del archivo >>")

    print(f"-Nombre del archivo: {archivo.name}")
    print(f"-Modo de apertura: {traducir_modo_apertura(archivo.mode)}")

    estado = "Cerrado" if archivo.closed else "Abierto"
    print(f"-Estado del archivo: {estado}")

    info_archivo = os.stat(archivo.name)
    tamagno = info_archivo.st_size  # Tamaño en Bytes
    print(f"-Peso del archivo: {tamagno} Bytes")

    centrar_titulo("<< Contenido del archivo >>")

    if tamagno == 0:
        imprimir_contenido("Archivo sin contenido...")

    elif tamagno <= 500:

        print("= Leyendo contenido con read()\n")
        imprimir_contenido(archivo.read())

    else:
        print("= Leyendo contenido con readline()\n")
        print("=" * 70)
        linea = archivo.readline()

        while linea:
            print(linea)
            linea = archivo.readline()
        print("=" * 70)

    cerrar_archivo(archivo)

except FileNotFoundError:
    print("El archivo no existe")
