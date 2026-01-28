"""
1. Definir la clase Auto con atributos marca, color, velocidad
2. Inicializar el objeto con velocidad en 0
3. Agregar método acelerar() que aumente la velocidad
4. Agregar método frenar() que la disminuya
5. Mostrar el estado del objeto antes y después de ejecutar métodos
6. Ver cómo cada objeto mantiene su propio estado independiente
Objetivo: entender cómo los métodos afectan el estado interno de un objeto a través de sus atributos.
"""

class Auto:
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
        self.velocidad = 0

    def acelerar(self,aumento):
        if aumento <= 0:
            print("El aumento de velocidad debe ser mayor a 0.")
            return
        self.velocidad += aumento 


    def frenar(self, disminucion):
        if disminucion <= 0:
            print("La disminución de velocidad debe ser mayor a 0.")
            return
        self.velocidad -= disminucion
        
        if self.velocidad < 0:
            self.velocidad = 0

    def mostrar_estado(self):
        print(f"Marca: {self.marca} | Color: {self.color} | Velocidad: {self.velocidad}")


auto1 = Auto("Toyota", "Blanco")
auto2 = Auto("Nissan", "Negro")

auto1.mostrar_estado()
auto2.mostrar_estado()
print("==================================")
auto1.acelerar(60)
auto2.acelerar(90)

auto1.mostrar_estado()
auto2.mostrar_estado()
print("==================================")
auto1.frenar(30)

auto1.mostrar_estado()
auto2.mostrar_estado()

'''
1. Crear la clase Automovil con atributos internos: encendido, combustible, velocidad
2. Definir método encender() que:
● Verifique si hay combustible
● Cambie el estado encendido a True
● Muestre un mensaje al usuario
3. Definir método acelerar() que:
● Aumente la velocidad
● Reste combustible
● Muestre un mensaje amigable
4. Ocultar detalles internos (cálculos, chequeos, lógica condicional)
'''

class Automovil:
    def __init__(self, combustible):
        self.encendido = False
        self.combustible = combustible
        self.velocidad = 0

    def encender(self):
        if self.encendido:
            print("Ya estoy encendido...")
            return

        if self.combustible <= 0:
            print("No puedo encender: no hay combustible")
            return
        
        self.encendido = True
        print("brum brummmm: Automóvil encendido...")


    def acelerar(self, aumento):
        if not self.encendido:
            print("No estoy encendido, no puedo aumentar velocidad...")
            return
        
        if self.combustible <= 0:
            print("Sin combustible, no puedo acelerar...")
            self.encendido = False
            return

        if aumento <= 0:
            print("El aumento de velocidad debe ser mayor a 0.")
            return
        
        velocidad_aux = self.velocidad
        self.velocidad += aumento
        combustible_aux = self.combustible
        self.combustible -= 18

        if self.combustible <= 0:
            print("Sin combustible suficiente, no puedo acelerar...")
            print(f"Se intento acelerar {aumento} pero sólo había {combustible_aux} de combustible")
            self.combustible = combustible_aux
            self.velocidad = velocidad_aux
            return

        print(f"Acelerando... Velocidad actual: {self.velocidad} k/m | Combustible: {self.combustible}")
        


auto1 = Automovil(20)
auto1.encender()
auto1.acelerar(80)
auto1.encender()     
auto1.acelerar(50)   
        

auto1.velocidad(200)