"""
-Asociación Simple: Una clase usa o conoce a otra, pero no depende de ella para existir

La Persona tiene una Direccion, pero ambas pueden existir por separado
"""
#Ejemplo:  Persona ---Usa --->Dirección

class Direccion:
    def __init__(self, calle, ciudad):
        self.calle = calle
        self.ciudad = ciudad

class Persona:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion

direccion = Direccion("Av. Alemania", "Temuco")
persona = Persona("Juan", direccion)

"""
-Agregación: Relación todo-parte débil: Las partes pueden existir sin el todo

Si el Equipo desaparece, los juagadores siguen existiendo
"""
#Ejemplo: Equipo <>----Jugador
class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
    
class Equipo:
    def __init__(self,nombre):
        self.nombre = nombre
        self.jugadores = []
    
    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

jugador_uno = Jugador("Pedro")
jugador_dos = Jugador("Luis")

equipo = Equipo("Colo-colo")
equipo.agregar_jugador(jugador_uno)
equipo.agregar_jugador(jugador_dos)


"""
-Composición: Relación todo-parte fuerte: Las partes no existen sin el todo

Las habitaciones nacen y mueren con la Casa
"""
#Ejemplo: Casa <+>----Habitación


class Habitacion:
    def __init__(self, nombre):
        self.nombre = nombre


class Casa:
    def __init__(self):
        self.habitaciones = [
            Habitacion("Dormitorio"),
            Habitacion("Cocina"),
            Habitacion("Baño")
        ]


casa = Casa()

for h in casa.habitaciones:
    print(h.nombre)


"""
-Herencia (Generalización): Una clase hereda atributos y métodos de otra

Auto es un Vehículo
"""
#Ejemplo: Vehículo <--- Auto


class Vehiculo:
    def __init__(self, marca):
        self.marca = marca
    
    def moverse(self):
        print("El vehículo se está moviendo")



class Auto(Vehiculo):
    def __init__(self, marca, puertas):
        super().__init__(marca)
        self.puertas = puertas


auto = Auto("Toyota", 4)
auto.moverse()

"""
-Dependencia: Una clase usa temporalmente a otra (por ejemplo, en un método).

Factura depende de Impresora, pero no la guarda como atributo.
"""
#Ejemplo: Factura ---> impresora

class Impresora:
    def imprimir(self, texto):
        print(texto)


class Factura:
    def generar_factura(self, impresora):
        impresora.imprimir("Factura generada")

"""
-Asociación con multiplicidad (1 a muchos):Una clase se relaciona con varias instancias de otra.

Un Estudiante puede tener muchos Cursos.
"""
#Una clase se relaciona con varias instancias de otra.

class Curso:
    def __init__(self, nombre):
        self.nombre = nombre


class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cursos = []
        

    def inscribir(self, curso):
        self.cursos.append(curso)


c1 = Curso("Programación")
c2 = Curso("Bases de Datos")

e = Estudiante("Ana")
e.inscribir(c1)
e.inscribir(c2)
