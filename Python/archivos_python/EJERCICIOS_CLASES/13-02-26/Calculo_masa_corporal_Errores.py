'''
🧩 Ejercicio: Calculadora de índice de masa corporal (IMC) con validación
📌 Contexto

Una aplicación de salud necesita calcular el Índice de Masa Corporal (IMC) de una persona.
Sin embargo, los usuarios suelen ingresar valores incorrectos o textos en lugar de números.

✅ Consigna
Crear un programa en Python que:
-Solicite el peso en kilogramos.
-Solicite la altura en metros.
-Verifique que ambos valores sean numéricos válidos.
-No permita valores negativos o cero.
-Calcule el IMC usando la fórmula:


IMC= peso/(altura)^2
	
Muestre la categoría:

-Bajo peso (< 18.5)
-Normal (18.5 – 24.9)
-Sobrepeso (25 – 29.9)
-Obesidad (≥ 30)

Si ocurre un error, mostrar un mensaje amable y permitir reintentar.
'''



while True:
    try:
        peso = float(input("Ingrese su peso: "))
        altura =  float(input("Ingrese su altura: "))

        imc = peso /(altura)**2

        if imc < 18.5:
            print(f"Indice de peso corporal: {imc:.2f}. Usted está en la categoría: Bajo peso")
        elif  imc< 25:
            print(f"Indice de peso corporal: {imc:.2f}. Usted está en la categoría: Normal")
        elif  imc< 30:
            print(f"Indice de peso corporal: {imc:.2f}. Usted está en la categoría: Sobrepeso")
        else:
            print(f"Indice de peso corporal: {imc:.2f}. Usted está en la categoría:  Obesidad")

        break

    except ValueError:
        print("Ingrese un número válido")