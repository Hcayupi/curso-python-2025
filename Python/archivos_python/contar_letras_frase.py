'''
4) Contar letras de una frase (ignorando espacios)

Enunciado:
Pide una frase al usuario y crea un diccionario con cuántas veces aparece cada letra.
Ignora los espacios y cuenta todo en minúscula.

Ejemplo: "Hola hola" → {'h':2,'o':2,'l':2,'a':2}
'''

diccionario_letras={}

def contar_letras(frase):
    diccionario_letras[frase]={}
    for letra in frase:
        if letra!= " ":
            if letra in diccionario_letras[frase]:  
                diccionario_letras[frase][letra]+=1 
            else:
                diccionario_letras[frase][letra]=1 # "hola hola":{h:2}

def listar_diccionario_frases():

    for frase, letras in diccionario_letras.items():
        print(f"- {frase} , {letras} ")

while True:

    frase_usuario = input("\n + Ingrese una frase o presione ENTER: ")
    
    if frase_usuario == "" : 
        break

    contar_letras(frase_usuario)
    print("\n")
    listar_diccionario_frases()
