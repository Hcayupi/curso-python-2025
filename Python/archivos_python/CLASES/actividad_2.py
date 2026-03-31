"""
1) Suma de múltiplos de 3 (0 a 300)
Enunciado: Suma todos los números entre 0 y 300 que sean múltiplos de 3 
e imprime la suma final.
"""
suma=0
for i in range(300):
    if i%3==0:
      suma += i;

print(suma)  


"""
2) Suma de los números que terminan en 7

Enunciado: Suma los números del 1 al 200 que terminan en 7 (7, 17, 27, …, 197) 
y muestra la suma.
"""
suma=0
for i in range(7,201,10):
    print(i)
    suma+=i
print("TOTAL: ", suma)


"""
3) “Fizz” y “Buzz” (1 a 60)

Enunciado: Imprime del 1 al 60.

Si es divisible por 3, imprime "Fizz"
Si es divisible por 4, imprime "Buzz"
Si es divisible por 3 y 4, imprime "FizzBuzz"
Si no, imprime el número.
"""

for i in range(1,60):
   if i%3==0:   
      print("Fizz")
   else:
        if i%4==0:
            print("Buzz")
        else:
            if i%3==0 and i%4==0:
                print("FizzBuzz")
            else: print(i)
"""
4) Contar cuántos son pares e impares

Enunciado: Recorre del 1 al 100 y cuenta cuántos números son pares 
y cuántos son impares. Muestra los totales.
"""
contador_par=0
contador_impar=0
for i in range(1,100):
    if i%2==0:
        print("Par: ",i) 
        contador_par+=1
    else:
        contador_impar+=1 
        print("Impar: ",i) 

print("Total pares: ", contador_par)
print("Total impares: ", contador_impar)
