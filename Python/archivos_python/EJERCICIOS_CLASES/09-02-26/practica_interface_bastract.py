from abc import ABC, abstractmethod

class SerVivo(ABC):
    
    @abstractmethod
    def nacer(self):
        pass

    @abstractmethod
    def crecer(self):
        pass

    @abstractmethod
    def morir(self):
        pass


class Animal(SerVivo):

    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    
    def comer(self):
        print(f"{self.__nombre} está comiendo")

    def describeme(self):
        print("Soy un animal del tipo", type(self).__name__)
    
    @abstractmethod
    def hacer_sonido(self):
        pass

    def get_nombre(self):
        return self.__nombre

class Planta(SerVivo):

    def __init__(self, tipo, edad):
        self.__tipo = tipo
        self.__edad = edad
    
    def fotosintesis(self):
        print("La planta realiza fotosintesis")


class Perro(Animal):

    def nacer(self):
        print("El perro nace")
    
    def crecer(self):
        print("El perro crece")
    
    def morir(self):
        print("El perro muere")
    
    def hacer_sonido(self):
        print("Guau")

class Arbol(Planta):

    def nacer(self):
        print("El árbol brota")
    
    def crecer(self):
        print("El árbol crece")

    def morir(self):
        print("El árbol se seca")

p = Perro("Firulais", 3)
p.nacer()
p.comer()
p.hacer_sonido()
p.describeme()


a = Arbol("Roble", 10)
a.fotosintesis()
a.crecer()