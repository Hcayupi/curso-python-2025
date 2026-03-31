from abc import ABC, abstractmethod

class Animal:               #Clase padre
    pass

class Perro(Animal):        #Clase hija llama a la clase padre con ()
    pass

print(Perro.__bases__)


#===========HERENCIA==============
class Animal(ABC):
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad
    
    # Método genérico pero con implementación particular
    @abstractmethod
    def hablar(self):
        # Método vacío
        pass

    # Método genérico pero con implementación particular
    @abstractmethod
    def moverse(self):
        # Método vacío
        pass

    # Método genérico pero con implementación particular
    def describeme(self):
        print("Soy un animal  del tipo", type(self).__name__)

"""
Hereda
Class perro no tiene constructo, pero usa el de animal
el metodo describeme fue definido en la clase padre
el objeto mi_perro puede usarlo 
entonces la class hija no necesita reescribir todo
"""
class Perro(Animal):
    pass

mi_perro = Perro("mamífero", 5)
mi_perro.describeme()


#===============SOBRESCRIBE============
"""
Sobreescribir codigo 
agregamos hablar, ahora todos los animales pueden hablar, 
pero no hablan igual, cada clase hija sobreescribe el metodo,
es decir tienen el mismo metodo pero distinto comportamiento.
"""
class Animal:
    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        print("Guau!")

class Vaca(Animal):
    def hablar(self):
        print("Muuu!")


#==============AGREGA METODO NUEVO===============0
"""
Se agrega nuevo metodo a la clas hija( Abeja), y ese metodo
es picar() que no existe en class Animal solo en la class Abeja,
donde las clases hijas pueden agregar cosas propias
"""

class Animal:
    pass

class Abeja(Animal):
    def picar(self):
        print("Picar!")

#============USO DE SUPER==================
class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

# Con el mismo ejemplo, si queremos agregamos otro atributo en el constructor 
#a la clase Perro, pero para evitar codigo tenemos dos alternativas 
#?Alternativa 1 : se crea un nuevo __init__ y guarda las atributo
class Perro(Animal):
    def __init__(self, especie, edad, dueño):
        # self.especie = especie
        # self.edad = edad
        # self.dueño = dueño


#?Alternativa 2: o podemos usar super() para llamar al __init__ 
#?de la clase padre y asignar un nuevo atributo
        super().__init__(especie, edad)
        self.dueño = dueño

#Instancia
mi_perro = Perro('mamífero', 7, 'Luis')
mi_perro.especie
mi_perro.edad
mi_perro.dueño


#===============HERENCIA MULTIPLE=================
"""
La herencia múltiple ocurre cuando una clase hija hereda de más de
una clase padre al mismo tiempo.
En vez de heredar solo de Animal, Perro puede heredar de Animal y 
otra clase más.
"""
#Clase padre 1 : Animal
class Animal:
    def respirar(self):
        print("El animal está respirando")

#Clase padre 2: Mascota
class Mascota:
    def jugar(self):
        print("La mascota está jugando")

#Clase hija: Perro(Herencia multiple)
class Perro(Animal, Mascota):
    def ladrar(self):
        print("El perro está ladrando")

#Uso de las clases
perro = Perro()

perro.respirar()  # método heredado de Animal
perro.jugar()     # método heredado de Mascota
perro.ladrar()    # método propio de Perro



#====================== MRO ===========================
#Orden de resolucion de metodos.
"""
Cuando una clase tiene herencia múltiple y dos clases 
padre tienen métodos con el mismo nombre, Python necesita
saber cuál usar.
El MRO define el orden en que Python busca esos métodos.

"""
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

#Salida en consola 
"""[<class '__main__.Perro'>,
<class '__main__.Animal'>,
<class '__main__.Mascota'>,
<class 'object'>]"""
