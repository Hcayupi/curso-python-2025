class Producto:
    def __init__(self, nombre:str, precio:float):
        self.nombre = nombre
        self.precio = precio

class Usuario:
    def __init__(self, nombre:str, email:str):
        self.nombre = nombre
        self.email = email

    def login():
        pass


class Carrito:
    def __init__(self):
        self.__productos = []
    
    def agregar_producto(self, producto):
        self.__productos.append(producto)
    
    def calcular_total(self):
        pass
