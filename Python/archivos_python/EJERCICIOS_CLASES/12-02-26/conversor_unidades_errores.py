'''
Conversor de unidades con validación
Contexto:
En una aplicación de cálculo de distancias, necesitamos convertir kilómetros a millas. Sin embargo, la
entrada del usuario no siempre es válida, y puede generar errores si no se maneja correctamente.
Consigna:
Implementá un programa en Python que:
● Solicite al usuario una distancia en kilómetros
● Verifique si la entrada es numérica válida
● Convierta el valor a millas (1 km = 0.621371
mi)
● Muestre un mensaje de error si el valor
ingresado no es un número

Paso a paso:
1. Usá un bloque try/except para capturar
ValueError
2. Si es válida, hacé la conversión y mostrala
con 2 decimales
3. Si falla, mostrale un mensaje amable al
usuario
4. Podés usar un bucle para reintentar hasta
que ingrese bien
'''

print("="*10, "Conversor de unidades", "="*10)

while True:
    try:
        kilometros = int(input("Ingrese los kilómetros de distancia: "))

        millas = kilometros * 0.621371

        print(f"Conversión a millas: {millas:.2f}")

        break

    except ValueError:
        print("Error de casteo.")