
"""2. Determinar si un número es par, impar o múltiplo de 3
a. Pide al usuario un número entero.
b. Convierte la entrada con int.
c. Usa una condición if con un operador lógico (and) para verificar si el número es divisible por
2 y por 3.
d. Si no se cumple, agrega más condiciones para verificar si es par solamente, o si es impar y
múltiplo de 3.
e. En el caso contrario, indica que es impar y no múltiplo de 3.
f. Usa mod (%) para evaluar divisibilidad."""


numero = int(input("Ingrese un número: "))

if numero%2==0 and numero%3==0:
    print("Número divisible por 2 y por 3")
else:
     if numero%2 == 0:
        print("El número es par")
     elif numero%2!=0 and numero%3==0:
         print("El número es impar y multiplo de 3")
     elif numero%2!=0 and not(numero%3==0):
         print("El número es impar y no multiplo de 3")



"""3. Clasificación de edades
a. Pide al usuario que ingrese su edad.
b. Convierte la entrada a entero (int).
c. Verifica que sea un número válido (mayor o igual a cero).
d. Si la edad es de 0 a 12, imprime que es un niño o niña.
e. Si está entre 13 y 17, indica que es adolescente.
f. Si está entre 18 y 64, que es adulto.
g. Si tiene 65 años o más, clasificalo como adulto mayor.
h. Muestra el resultado final en pantalla."""

numero = int(input("Ingrese su edad: "))

if numero >= 0:
    if numero >= 0 and numero <= 12:
        print("Es un niño o niña")
    else:
        if numero >= 13 and numero <= 17:
            print("Es adolescente")
        else:
            if numero >= 18 and numero < 65:
                print("Es adulto")
            else:
                if numero >= 65:
                    print("Es adulto mayor")
else:
    print("No es un número válido")


nombres = ["Ana", "Pedro", "Luis", "Pedro"]

for nombre in nombres:
    if nombre == "Luis":
        print(nombre)
        break
    else:
        print("No es Luis")