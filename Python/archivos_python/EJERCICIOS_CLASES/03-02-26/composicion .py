'''
Vas a diseñar una clase principal que contenga otras clases como parte de su estructura, representando una
relación de composición real.

Qué debe tener cada clase:
➔ Clase Procesador:Atributos: marca, velocidad_ghz
➔ Clase MemoriaRAM:Atributos: capacidad_gb, tipo
➔ Clase DiscoDuro:Atributos: capacidad_gb, tipo (HDD/SSD)
➔ Clase Computadora:Atributos: marca, y objetos de tipo Procesador, MemoriaRAM, DiscoDuro
◆ Método mostrar_info() que imprima todos los datos, incluyendo los de sus componentes
Qué se debe probar:
● Crear instancias individuales de los componentes
● Crear una Computadora pasándole esos objetos
● Usar el método mostrar_info() para mostrar toda la información en conjunto
'''

class Procesador:

    def __init__(self, marca, velocidad_ghz):
        self.marca = marca
        self.velocidad_ghz = velocidad_ghz
    
    def  __str__(self):
        return f"{self.marca} - {self.velocidad_ghz} Ghz" 

class MemoriaRAM:

    def __init__(self, capacidad_gb, tipo):
        self.capacidad_gb = capacidad_gb
        self.tipo = tipo

    def __str__(self):
        return f"{self.capacidad_gb}GB -{ self.tipo}"

class DiscoDuro:

    def __init__(self, capacidad_gb, tipo):
        self.capacidad_gb = capacidad_gb
        self.tipo  = tipo
    
    def __str__(self):
        return f"{self.capacidad_gb}GB -{ self.tipo}"
    
class Computadora:

    def __init__(self, marca, procesador, memoria_ram, disco_duro):
        self.marca = marca
        self.procesador = procesador
        self.memoria_ram = memoria_ram
        self.disco_duro = disco_duro
    
    def mostrar_info(self):
        print("Información de computadora")
        print(f"Marca: {self.marca}")
        print(f"Procesador: {self.procesador}")
        print(f"Memoria RAM: {self.memoria_ram}")
        print(f"Disco Duro: {self.disco_duro}")



procesador = Procesador("Intel", 3.6)
memoriaRam = MemoriaRAM(16, "DDR4")
disco_duro = DiscoDuro(512, "SSD")

print("==== Creando la computadora con sus componentes ====")
computadora = Computadora("Lenovo", procesador, memoriaRam, disco_duro)

computadora.mostrar_info()

"""
Entre vehículo y gasolina NO hay una relación de composición.
La relación correcta es una colaboración (uso / dependencia).

¿Por qué no es composición?

En una composición, una clase forma parte de la otra y no puede existir por separado.
Ejemplos clásicos:

Vehículo 🚗 — Motor

Casa 🏠 — Habitaciones

Si el vehículo desaparece, el motor deja de tener sentido dentro de ese contexto.
"""