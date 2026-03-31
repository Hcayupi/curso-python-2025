"""
Gestor de archivos seguro
Contexto:
Queremos desarrollar una mini herramienta en Python que permita escribir datos en un archivo, moverlo a
una carpeta nueva y garantizar su manejo seguro, contemplando posibles errores.
Consigna:
Implementá un programa en Python que:
● Solicite al usuario un nombre de archivo y un contenido para escribir
● Cree o sobrescriba el archivo usando with open() en modo "w"
● Escriba el contenido proporcionado
● Cree una carpeta llamada "backup" si no existe (usá os.makedirs())
● Mueva el archivo a la carpeta "backup/" usando shutil.move()
● Utilice try/except/finally para:
○ Capturar posibles errores (FileNotFoundError, PermissionError)
○ Garantizar el cierre correcto del archivo y mostrar un mensaje final

Tiempo : 40 Minutos

Gestor de archivos seguro
Paso a paso:
1. Pedir el nombre del archivo y el contenido al usuario
2. Escribir el contenido en el archivo usando with open()
3. Crear la carpeta "backup" si no existe (os.makedirs("backup", exist_ok=True))
4. Mover el archivo recién creado a "backup/"
5. Asegurarse de capturar cualquier error que ocurra
6. Mostrar un mensaje final como "Operación finalizada" en un bloque finally
"""

import os
import shutil

os.system("cls")
print()
nombre_archivo = input("Ingrese nombre del archivo: ")
print("\n = Escriba el contenido del archivo = \n")
print("-" * 40)
contenido_archivo = input()
print("-" * 40)

try:
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write(contenido_archivo)

    carpeta_respaldo = "backup"
    os.makedirs(carpeta_respaldo, exist_ok=True)

    ruta_destino = os.path.join(carpeta_respaldo, nombre_archivo)
    shutil.move(nombre_archivo, ruta_destino)

    print()
    print("Archivo movido correctamente...")

    if archivo.closed:
        print("Archivo cerrado correctamente...")

except FileNotFoundError:
    print("Archivo no existe.")

except PermissionError:
    print("No tienes permisos para realizar esta operación.")

except Exception as e:
    print("Error inesperado:", e)

except OSError as e:
    print(f"Error de sistema: {e}")

finally:
    print()
    print(" = Operación finalizada. =")
    print()
