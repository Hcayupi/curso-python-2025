class Animal:
    def sonido(self):
        print("Sonido de animal")

class Mascota:
    def sonido(self):
        print("Sonido de mascota")

class Perro(Animal, Mascota):
    pass

perro = Perro()
perro.sonido()

#Imprime en consola #? Sonido de animal
"""
Porque Python sigue el MRO y busca los métodos de izquierda
a derecha según el orden en que las clases padre fueron 
declaradas
En este caso:

1.-Perro
2.-Animal
3.-Mascota
4.-object

"""
#!Cómo ver el MRO en Python
print(Perro.mro())