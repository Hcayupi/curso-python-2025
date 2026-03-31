# ? Ejercicio 2

class Cliente:
    def __init__(self, nombre, email):
        self.__nombre = nombre
        self.__email = email
        self.carrito = Carrito()

    def comprar():
        pass

class Producto:
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        self.__precio=precio


class Carrito:
    def __init__(self):
        self.__productos = list[Producto] = []

    def agregar(self, producto):
        pass

    def vaciar():
        pass



class Factura:
    def __init__(self, total):
        self.total = total

    def imprimir(carrito):
        pass




cliente = Cliente("Alberto", "d@gmail.com")

producto = Producto("Mate", 500)

cliente.comprar()

cliente.carrito.agregar(producto)

