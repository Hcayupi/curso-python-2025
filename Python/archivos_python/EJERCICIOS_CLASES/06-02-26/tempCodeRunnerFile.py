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

    #contador para recorrer texto/palabra de izquierda a derecha
    texto = texto.lower() #convierte todo a minúscula
    largo_texto= len(texto)
    indice_izquierda = 0
    indice_derecha = largo_texto-1

    while indice_izquierda < largo_texto:

        if texto[indice_izquierda] == " ":
            indice_izquierda+=1
        if texto[indice_derecha] == " ":
            indice_derecha-=1

        if letra_sin_tilde(texto[indice_izquierda]) != letra_sin_tilde(texto[indice_derecha]):
                return False

        indice_derecha-=1
        indice_izquierda +=1

    return True

#Función externa
def analizar_texto(texto):

    if es_palindromo(texto):
        print("Es un palíndromo")
    elif es_palindromo(texto)==False:
        print("No es un palíndromo")   

analizar_texto("Adán no cede con Eva Yavé no cede con nada")
