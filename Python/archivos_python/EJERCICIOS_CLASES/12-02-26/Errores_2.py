try:
    print("=== Caso 1 Error de sintaxis ===")
    if True:
        print("Esto no se ejecutará")
except Exception as e:
    print("Error", e)

try:
    print("=== Caso 2 Excepción en tiempo de ejecución ===")
    print("Inicio del programa")
    numero = int("abc")
    print("Esto no se verá")
    
except ValueError as e:
    print(f"se capturo un ValueError: {e}")

except Exception as e:
    print("Error", e)