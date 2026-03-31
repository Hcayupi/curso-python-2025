# ?Ejercicio 1

class Pasajero:
    def __init__(self, nombre, dni, email):
        self.nombre = nombre
        self.dni = dni
        self.email = email


class Reserva:
    def __init__(self, codigo, fecha, estado):
        self.codigo = codigo
        self.fecha = fecha
        self.estado = estado


class Vuelo:
    def __init__(self, origen, destino, hora, avion):
        self.origen = origen
        self.destino = destino
        self.hora = hora
        self.avion = avion


class Avion:
    def __init__(self, modelo, capacidad):
        self.modelo = modelo
        self.capacidad = capacidad


avion = Avion("hhasd", 21324)

vuelo=Vuelo("asdasd", "asdasda", 234, avion)




reserva =  Reserva(1231, "123213", True)

pasajero = Pasajero("asdad",12313, "f@gamil.com")
