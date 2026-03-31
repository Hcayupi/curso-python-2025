'''
Contexto:
Vas a diseñar un sistema para representar diferentes tipos de medios de transporte.
Consigna:
Implementá las siguientes clases en Python usando
herencia:
Vehiculo (clase base): marca, modelo, moverse()
Auto (subclase): sobrescribe moverse() con "Conduciendo
por la carretera"
Bicicleta (subclase): sobrescribe moverse() con
"Pedaleando"
Motocicleta (subclase): agrega atributo cilindrada

Paso a paso:
1. Aplicar herencia simple
2. Usar sobrescritura de métodos
3. Probar comportamiento polimórfico con
un bucle que recorra una lista de vehículos
y llame a moverse()
'''

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo=modelo
    
    def moverse(self):
        print("Voy en la ruta...")

class Auto (Vehiculo):

    def moverse(self):
        print("Conduciendo por la carretera")

class Bicicleta(Vehiculo):

    def moverse(self):
        print("Pedaleando")

class Motocicleta(Vehiculo):
    def __init__(self,marca,modelo, cilindrada):
        super().__init__(marca,modelo)
        self.cilindrada = cilindrada

lista_vehiculos = [
    Auto("Subaru", "Impreza"), 
    Bicicleta("Oxford", "12334"), 
    Motocicleta("Honda", "x650","150cc")]


for vehiculo in lista_vehiculos:

    print(f"{vehiculo.marca} : ")
    vehiculo.moverse()
    