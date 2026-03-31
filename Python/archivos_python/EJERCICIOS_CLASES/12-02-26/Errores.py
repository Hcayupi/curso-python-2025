try:
    numero = int(input("Ingresar numero: "))
    resultado = 10 / numero
    print(f"Resultado: {resultado}")

except ValueError:
    print("Error: Debe ser un número entero")

except ZeroDivisionError:
    print("Error: No se puede dividir por cero")



################ ejercicio 2
try:
    # ZeroDivisionError
    print(10 / 0)
except ZeroDivisionError:
    print("Division por cero")

try:
    # ValueError
    edad = int("veinticinco")
except ValueError:
    print("Error en el casteo")

try:
    # IndexError
    lista = [1, 2, 3]
    print(lista[5])
except IndexError:
    print("Error de indice")

try:
    # KeyError
    datos = {
        "nombre": "ana",
        "edad": 20 
    }
    print(datos["apellido"])
except KeyError:
    print("Error de key")

try:
    # TypeError
    resultado = "10" + 5
except TypeError:
    print("Error de tipo")