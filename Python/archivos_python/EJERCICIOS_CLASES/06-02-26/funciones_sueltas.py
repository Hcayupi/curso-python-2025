'''
Función suelta #1: mezclar_textos()

Objetivo: practicar *args + defaults + condicionales.

Enunciado
Crea una función mezclar_textos(*args, separador=" ", mayus=False) que:

* Reciba cualquier cantidad de textos (strings) por *args.
* Si no recibe textos, debe retornar "Sin textos".
* Una los textos usando el separador.
* Si mayus=True, el resultado debe quedar en mayúsculas.
* Retorne el texto final.

Casos de prueba esperados:
* mezclar_textos("hola", "mundo") → "hola mundo"
* mezclar_textos("hola", "mundo", separador="-") → "hola-mundo"
* mezclar_textos(mayus=True) → "Sin textos"
'''



def  mezclar_textos(*palabras, separador=" ", mayus=False):
        if len(palabras)==0:
                print("Sin texto")
                return
        cadena=""
        for palabra in palabras:
            cadena= cadena + palabra + separador
        """
        #rstrip elimina el ultimo separador: rstrip elimina tanto espacio o caracteres que estén al final
        #lstrip elimina al inicio
        """
        if mayus:
            print(cadena.rstrip(separador).upper())
        else:
            print(cadena.rstrip(separador))

#mezclar_textos("hola", "mundo") → "hola mundo"

mezclar_textos("perro", "gato", "conejo")

#mezclar_textos("hola", "mundo", separador="-")

mezclar_textos("perro", "gato", "conejo", separador="-")

#mezclar_textos(mayus=True)

mezclar_textos(mayus=True)


#mezclar_textos("hola", "mundo", separador="-")

mezclar_textos("perro", "gato", "conejo", separador="-", mayus=True)


'''
Función suelta #2: calcular_area()

Objetivo: practicar “sobrecarga” con **kwargs.

Enunciado

Crea una función calcular_area(**kwargs) que calcule el área según los datos entregados:
* Si llega radio=... → área del círculo.
* Si llega base=... y altura=... → área del triángulo.
* Si llega ancho=... y alto=... → área del rectángulo.
* Si no coincide con ninguno, debe retornar None y mostrar "Datos insuficientes".
* Validar que los valores sean positivos.

Casos de prueba esperados:
* calcular_area(radio=3) → 28.27...
* calcular_area(base=10, altura=5) → 25
* calcular_area(ancho=4,alto=4)
'''
import math


def validar_datos(clave_valor):
        for valor in clave_valor.values():
            if valor<=0:
                print("Los valores deben ser mayor a 0")
                return False
        return True


def calcular_area(**clave_valor):
        
        if not validar_datos(clave_valor):
            return
        
        if clave_valor.get("radio"):
            radio = clave_valor.get("radio")
            area_cirulo =  math.pi * radio**2
            print (f"Area del círculo: {area_cirulo}")
            return

        if clave_valor.get("base") and clave_valor.get("altura"):
            base = clave_valor.get("base")
            altura = clave_valor.get("altura")
            area_triangulo = (base *altura)/2
            print(f"Área del triángulo: {area_triangulo}")
            return
        
        if clave_valor.get("ancho")  and clave_valor.get("alto"):
            ancho = clave_valor.get("ancho")
            alto = clave_valor.get("alto")
            area_rectangulo = ancho * alto
            print(f"Área de un rectángulo: {area_rectangulo}")
            return

        print("Datos insuficientes")
        return None


calcular_area(radio=-3)

calcular_area(base=0, altura=5) 

calcular_area()