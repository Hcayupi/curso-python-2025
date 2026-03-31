"""
Enunciado (repaso POO completo)

Vas a desarrollar un mini-sistema para una tienda:

1.- Producto
* Tiene atributo público nombre
* Tiene atributo “privado” __precio
* Tiene atributo de clase iva (parámetro de clase) con valor inicial 0.19
* Debe tener get_precio() y set_precio() (solo permite valores positivos)
* Debe tener precio_final() que calcule precio con IVA
* Debe implementar __str__ para que al imprimir el objeto muestre algo legible

2.- Método de clase (@classmethod)
* Debe existir un método cambiar_iva(nuevo_iva) que cambie el IVA para todos los productos

3.- Método estático (@staticmethod)
* Debe existir un método es_precio_valido(precio) que retorne True/False

4.- Carrito (composición)
* Una clase Carrito que “contenga” una lista de productos (parte esencial del carrito)
* Debe tener agregar_producto(producto) y mostrar()

5.- Método con “sobrecarga” simulada
* En Carrito, crea un método calcular_total(*args) que funcione así:
    - Si no recibe nada → total con IVA
    - Si recibe 1 argumento (con_iva) → si es False, calcula sin IVA
    - Si recibe 2 argumentos (con_iva, descuento) → aplica descuento % al final

6.- Colaboración
* Crea una clase Impresora con método imprimir_ticket(carrito)
* El carrito usa la impresora (no la contiene como parte ese
"""

class Producto:

    iva = 0.19 #Atributo de clase

    def __init__(self, nombre, precio):
        self.nombre=nombre
        self.__precio = precio
        self.set_precio(precio) #evaluación al crear un objeto
    
    def set_precio(self, nuevo_precio):
        if not Producto.es_precio_valido(nuevo_precio):
            print("Debe ingresar un precio válido")
            return 
        self.__precio = nuevo_precio
    
    def get_precio(self):
        return self.__precio

    def precio_final (self):
        #total = self.__precio * (1+Producto.iva)
        iva= self.__precio * Producto.iva
        total_con_iva = self.__precio + iva
        return total_con_iva
    
    @classmethod
    def cambiar_iva(cls, nuevo_iva):
        if not nuevo_iva>0 and not isinstance(nuevo_iva, (int,float)):
            print ("IVA inválido...")
            return
        
        cls.iva = nuevo_iva

    @staticmethod
    def es_precio_valido(precio):
        return isinstance(precio, int) and precio>0
    
    def __str__(self):
        return f"Producto: {self.nombre} | Precio: {self.__precio}"


class Carrito:

    def __init__(self):
        self.producto=[]

    def agregar_producto(self, producto):
        if not isinstance(producto, Producto):
            print("Producto ingresado no es válido")
            return
        self.producto.append(producto)

    def mostrar(self):
        if len(self.producto)==0:
            print("El carrito está vacío...")
            return
        for producto in self.producto:
            print(producto)

    """
    Método con “sobrecarga” simulada
* En Carrito, crea un método calcular_total(*args) que funcione así:
    - Si no recibe nada → total con IVA
    - Si recibe 1 argumento (con_iva) → si es False, calcula sin IVA
    - Si recibe 2 argumentos (con_iva, descuento) → aplica descuento % al final
    """

    def calcular_total (self, *args):
        con_iva = True
        descuento = None
        total = 0

        if len(args) == 1:
            con_iva = args[0]
        elif len(args) == 2:
            con_iva = args[0]
            descuento = args[1]
        elif len(args)>2:
            print("Error: máximo 2 parámetros  (con_iva, descuento)")
            return

        for producto in self.producto:
            if con_iva:
                total += producto.precio_final()
            else:
                total += producto.get_precio()
            
        
        if  descuento:
            total = total * (1-descuento/100)

        return total

class Impresora: #Colaboración

    def imprimir_ticket(self, carrito):
        print("="*5, "Ticket", "="*5)
        carrito.mostrar()
        print("="*15)
        print(f"TOTAL:${carrito.calcular_total()}")


p1 = Producto("Polera", 500)
p2 = Producto("Pantalon", 1000)
p3 = Producto("Gorro", 500)

carrito = Carrito()

carrito.agregar_producto(p1)
carrito.agregar_producto(p2)
carrito.agregar_producto(p3)

#carrito.calcular_total(True,50)

impimir = Impresora()
impimir.imprimir_ticket(carrito)