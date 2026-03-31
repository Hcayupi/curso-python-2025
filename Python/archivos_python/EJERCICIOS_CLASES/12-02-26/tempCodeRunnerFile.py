print("="*10, "Indice de masa corporal", "="*10)
try: 
    primer_numero = float(input("Ingrese  primer número:"))
    segundo_numero = float(input("Ingrese  segundo número:"))

    resultado_division = primer_numero/segundo_numero

    print (f"Resultado division: {resultado_division:.2f}")
except ValueError:
    print("Error en el casteo")
except ZeroDivisionError:
    print("Error división por 0")