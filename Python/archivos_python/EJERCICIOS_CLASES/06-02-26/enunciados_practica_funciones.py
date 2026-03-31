'''
1) Función: calculadora de propina y total
Enunciado

Crea una función calcular_propina_total(monto_cuenta, porcentaje_propina=10) que:

* Reciba el monto de la cuenta y el porcentaje de propina (opcional).
* Valide que monto_cuenta > 0 y porcentaje_propina >= 0.
* Retorne una tupla: (propina, total).

Ejemplos de uso:

calcular_propina_total(20000)          # propina 10% por defecto
calcular_propina_total(20000, 15)      # propina 15%

'''

def calcular_propina_total(monto_cuenta, porcentaje_propina=10):

    if not monto_cuenta>0 or not porcentaje_propina >=0:
        return()
    
    propina = monto_cuenta *porcentaje_propina/100
    total = monto_cuenta *(1 + porcentaje_propina/100)

    return (propina, total)

resultado_monto = calcular_propina_total(-20000)

if len(resultado_monto)==0:
    print("El monto y la propina deben mayores a 0")
else:
    print(f"PROPINA: {int(resultado_monto[0])}")
    print(f"MONTO TOTAL: {int(resultado_monto[1])}")


'''
2) Función: dividir cuenta entre amigos
Enunciado

Crea una función dividir_cuenta(total, personas) que:

* Reciba el total a pagar y la cantidad de personas.
* Valide que total > 0 y personas >= 1
* Retorne cuánto paga cada persona.

Ejemplos de uso:

dividir_cuenta(45000, 3)   # 15000
dividir_cuenta(10000, 1)   # 10000

'''

def dividir_cuenta(total, personas):
    if not total>0 or not personas >=1:
        print("La cuenta debe ser mayor a $0 y mínimo una persona")
        return 0
    
    division_monto = total/personas
    return division_monto

monto_repartido = dividir_cuenta(45000, 0)

if monto_repartido != 0:
    print(f"Cada persona debe pagar: ${int(monto_repartido)}")


'''
3) Función: precio final con descuento
Enunciado

Crea una función aplicar_descuento(precio, porcentaje_descuento) que:

* Valide que precio > 0 y 0 <= porcentaje_descuento <= 100.
* Calcule el precio final y lo retorne.
* (Opcional) Retorne también el monto descontado.

Ejemplos de uso:

aplicar_descuento(20000, 25)
aplicar_descuento(10000, 0)

'''

def aplicar_descuento(precio, porcentaje_descuento):
    if not precio>0:
        print("El precio debe ser mayor a 0")
        return ()
    if not(0<= porcentaje_descuento <=100):
        print("El porcentaje debe estar entre 0% y 100%")
        return ()
    
    monto_descontado = precio *porcentaje_descuento/100
    precio_final= precio * (1-porcentaje_descuento/100)

    #Para retornar dos valores fue necesario hacerlo con una tupla
    return (monto_descontado, precio_final)


precio_descuento = aplicar_descuento(20000, 25)

if len(precio_descuento) != 0:
    print(f"Descuento: ${int(precio_descuento[0])}")
    print(f"Total: ${int(precio_descuento[1])}")


'''
4) Función: convertir minutos a formato hh:mm
Enunciado

Crea una función minutos_a_hhmm(minutos) que:

* Reciba un entero minutos (>= 0).
* Convierta a horas y minutos.
* Retorne un string con formato "hh:mm" (dos dígitos).

Ejemplos de uso:

minutos_a_hhmm(135)   # "02:15"
minutos_a_hhmm(5)     # "00:05"

'''

def minutos_a_hhmm(minutos):
    if not minutos>=0: 
        return "Los minutos deben ser mayoe a 0"
    horas = minutos //60
    minutos_totales = minutos %60

    return f"{horas}:{minutos_totales}"

print(minutos_a_hhmm(5))



'''
5) Función: prioridad de atención (triage básico)
Enunciado

Crea una función prioridad_atencion(temperatura, dificultad_respiratoria) que:

* Reciba temperatura (float) y dificultad respiratoria (bool).
* Retorne "ALTA", "MEDIA" o "BAJA" según reglas:
    - ALTA si dificultad_respiratoria es True o temperatura >= 39
    - MEDIA si 37.5 <= temperatura < 39
    - BAJA si temperatura < 37.5 y sin dificultad respiratoria

Ejemplos de uso:

prioridad_atencion(39.2, False)  # "ALTA"
prioridad_atencion(38.0, False)  # "MEDIA"
prioridad_atencion(36.8, False)  # "BAJA"
prioridad_atencion(36.8, True)   # "ALTA"

'''

def prioridad_atencion (temperatura, dificultad_respiratoria):

    if not isinstance(temperatura, float):
        return "La temperatura debe ser en formato float"
    if not isinstance(dificultad_respiratoria, bool):
        return "Dificultad respiratoria debe ser True o False"
    
    if temperatura>=39 or dificultad_respiratoria:
        return "ALTA"
    if 37.5 <= temperatura < 39:
        return "MEDIA"
    if temperatura < 37.5 and dificultad_respiratoria == False:
        return "BAJA"

print (prioridad_atencion(39.2, False) ) # "ALTA"
print (prioridad_atencion(38.0, False) ) # "MEDIA"
print (prioridad_atencion(36.8, False) ) # "BAJA"
print (prioridad_atencion(36.8, True) )  # "ALTA"



'''
6) Función: calcular IMC y categoría
Enunciado

Crea una función calcular_imc(peso_kg, altura_m) que:

* Valide peso_kg > 0 y altura_m > 0.
* Calcule el IMC.
* Retorne una tupla (imc, categoria) con categorías:
    Bajo peso: < 18.5
    Normal: 18.5 a < 25
    Sobrepeso: 25 a < 30
    Obesidad: >= 30

Ejemplos de uso:

calcular_imc(70, 1.75)
calcular_imc(50, 1.70)

'''

def calcular_imc(peso_kg, altura_m):
    if not peso_kg > 0 or not altura_m > 0:
        print("Los valores deben ser mayores a 0")
        return ()
    
    imc = peso_kg /(altura_m**2)

    if imc < 18.5:
        return ("Bajo peso", imc)
    if  18.5 > imc <25:
        return ("Normal", imc)
    if 25 > imc <30:
        return ("Sobrepeso", imc)
    if imc >= 30:
        return("Obesidad", imc)

indice_masa_corporal = calcular_imc(50, 1.75)

if len(indice_masa_corporal) != 0:
    print(f"Categoría: {indice_masa_corporal[0]}")
    print(f"Peso:{round(indice_masa_corporal[1],2)}") #round: redondea a 2 decimales
'''
7) Función: detectar palíndromo (versión simple)
Enunciado

Crea una función es_palindromo(texto) que:

* Reciba un texto.
* Compare ignorando mayúsculas/minúsculas.
* Retorne True si es palíndromo, False si no.
* (Versión simple) No eliminar espacios ni tildes.

Ejemplos de uso:

es_palindromo("Radar")      # True
es_palindromo("Python")     # False

'''
def letra_sin_tilde(letra):

    letras_tilde = {
        'á':'a',
        'é':'e',
        'í':'i',
        'ó':'o',
        'ú':'u'
        }
    
    if letra in letras_tilde:
        return letras_tilde[letra]

    return letra

def es_palindromo ( texto):

    if not texto!= "":
        print("Ingrese un texto")
        return None

    texto = texto.lower() #convierte todo a minúscula
    largo_texto= len(texto)
    #contador para recorrer texto/palabra de izquierda a derecha
    indice_izquierda = 0
    indice_derecha = largo_texto-1

    while indice_izquierda < largo_texto:

        if texto[indice_izquierda] == " ":
            indice_izquierda += 1
        if texto[indice_derecha] == " ":
            indice_derecha -= 1

        if letra_sin_tilde(texto[indice_izquierda]) != letra_sin_tilde(texto[indice_derecha]):
                return False

        indice_derecha -= 1
        indice_izquierda += 1

    return True

#Función externa
def analizar_texto(texto):

    if es_palindromo(texto):
        print("Es un palíndromo")
    elif es_palindromo(texto)==False:
        print("No es un palíndromo")   

analizar_texto("Adán no cede con Eva Yavé no cede con nada")











