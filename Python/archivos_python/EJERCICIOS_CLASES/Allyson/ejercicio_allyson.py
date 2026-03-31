'''
Vas a diseñar una clase que represente un producto de tienda, 
controlando el acceso y modificación del precio a
través de métodos específicos.

1. Qué debe tener la clase:
● Un atributo público para el nombre del producto
● Un atributo privado para el precio (__precio)
● Un método para ver el precio (getter)
● Un método para modificar el precio (setter), 
que solo permita valores positivos
● En el constructor (__init__), usar el setter 
para validar el precio desde el inicio
2. Qué se debe probar con objetos:
● Crear un producto con precio válido
● Mostrar el precio usando el getter
● Intentar cambiar el precio a un valor negativo (debe mostrar un error)
● Modificar correctamente el precio y verificar el nuevo valor
'''
import os #

def limpiar_consola():
    os.system('cls')

class Producto:

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.__precio = 10
        self.set_precio(precio)
    
    def get_precio(self):
        return self.__precio
    
    def set_precio(self, nuevo_precio):
        if not self.precio_valido(nuevo_precio):
            print("Ingrese un precio mayor a 0")
            return
        self.__precio = nuevo_precio

    def __str__(self):
        return f"Producto: {self.nombre} | Precio: {self.__precio}"  #para imprimir nombre y precio
    
        
    def __lt__(self, otro_producto):
        return self.__precio < otro_producto.get_precio()

    @staticmethod
    def precio_valido(precio):
        return isinstance(precio, int) and precio > 0
        
class Carrito:

    descuento = 0.10

    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def ordenar_lista_productos(self):
        self.productos.sort()

    def mostrar_productos(self):        
        for producto in self.productos:
            print(producto)

    def buscar_producto(self, nombre_producto):
        #return next((p for p in self.productos if p.nombre == "Leche"),None)
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                return producto
        return None
    
    @classmethod
    def cambiar_valor_descuento(cls, nuevo_descuento):
        if not isinstance(nuevo_descuento, float) and  1 > nuevo_descuento < 0:
            print("descuento inválido, ingrese decimal mayor a 0 y menos a 1.0")
            return
        
        cls.descuento = nuevo_descuento
        print("Descuento aplicado")
    
    def precio_final(self):
        total = 0
        if len(self.productos) >= 2:
            for producto in self.productos:
                total += producto.get_precio()
            descuento = total * self.descuento
            total -= descuento
        return total
            

            

nuevo_ingreso = True

carro = Carrito() #Se crea una instancia de carro para muchos productos, por eso se crea afuera, sino se crearia n veces (por bucle while)

while True:
    if nuevo_ingreso:
        limpiar_consola()
        nombre_producto = input("Ingrese nombre del producto: ")
        ingresar_precio = int(input("Ingrese precio del producto: "))
        if ingresar_precio < 0:
            print("El precio debe ser mayor a 0")
        else:
            nuevo_producto= Producto(nombre_producto, ingresar_precio)
            carro.agregar_producto(nuevo_producto)
            print("Producto creado con éxito")
            respuesta = input("Desea ingresar otro producto? S / N : ") 
            if respuesta == "N":
                print("Saliendo...")
                nuevo_ingreso = False
                break


carro.ordenar_lista_productos()
carro.mostrar_productos()

# seleccione_producto = input("Seleccione un producto para cambiar su precio: ")

# producto_buscado = carro.buscar_producto(seleccione_producto)
# if producto_buscado == None:
#     print("Producto no existe")
# else:
#     nuevo_precio_admin = int(input("Ingrese nuevo precio: "))
#     producto_buscado.set_precio(nuevo_precio_admin)
#     print(producto_buscado.get_precio())


#print(carro.precio_final())