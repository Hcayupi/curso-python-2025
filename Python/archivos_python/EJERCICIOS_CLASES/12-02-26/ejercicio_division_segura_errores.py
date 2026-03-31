'''
Contexto:
Muchos programas realizan cálculos entre números. La división es una operación común, pero puede
romperse si los datos no están controlados correctamente.
Consigna:
Creá una función que:
● Pida al usuario dos números
● Intente dividir el primero por el segundo
● Maneje dos errores posibles:
● Entrada inválida (ValueError)
● División por cero (ZeroDivisionError)
Imprima mensajes personalizados para cada uno


Paso a paso:
1. Capturá cada excepción en un bloque
separado
4. Probalo con entradas correctas y con

'''

print("="*10, "División Segura", "="*10)
try: 
    primer_numero = int(input("Ingrese  primer número:"))
    segundo_numero = int(input("Ingrese  segundo número:"))

    resultado_division = primer_numero/segundo_numero

    print (f"Resultado division: {resultado_division:.2f}")
except ValueError:
    print("Error en el casteo")
except ZeroDivisionError:
    print("Error división por 0")