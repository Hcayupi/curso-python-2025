import os
from tabulate import tabulate

def limpiar_consola():
    os.system('cls')

carrito_compras = {}

tabla = []

lista_de_productos = {
    "manzana": {"precio": 500,"stock": 4 },
    "pan": {"precio": 1200,"stock": 2},
    "leche": {"precio": 900,"stock": 1},
    "arroz": {"precio": 1800,"stock": 2},
    "fideos": {"precio": 1100,"stock": 3},
    "aceite": {"precio": 3500,"stock": 1},
    "azúcar": {"precio": 1300,"stock": 2},
    "sal": {"precio": 600,"stock": 1},
    "huevos": {"precio": 4200,"stock": 1},
    "queso": {"precio": 5500,"stock": 1}
}


def listar_producto():
    print ("---- LISTA DE PRODUCTOS DISPONIBLES ---- \n ")  
    for nombre, productos in lista_de_productos.items():
            tabla.append([nombre, productos["precio"], productos["stock"]])
    
    print(tabulate(tabla, headers=["Nombre", "Precio", "Stock"], tablefmt="grid"))
    tabla.clear()
    # print(f"   {nombre:<13}   {str(productos["precio"]):<8}   {productos["cantidad"]:<8} ") 


def mostrar_carrito():
    print ("\n      ----  CARRITO  ----")  
    for nombre, productos in carrito_compras.items():
        tabla.append([nombre, productos["precio"], productos["stock"]])
        #print(f"   {nombre:<13}   {str(productos["precio"]):<8}   {productos["cantidad"]:<8} ")
    print(tabulate(tabla, headers=["Nombre", "Precio", "Stock"], tablefmt="grid"))
    tabla.clear()
    

def agregar_al_carrito(producto, cantidad):
    cantidad_compra = 1
    if producto in lista_de_productos:
        if cantidad>0:
            cantidad_stock = int(lista_de_productos[producto]["stock"])

            if cantidad_stock == 0 or cantidad > cantidad_stock:
                return False
            
            cantidad_stock-=cantidad
            lista_de_productos[producto]["stock"]=cantidad_stock
            if producto in carrito_compras:
                cantidad_compra = carrito_compras[producto]["stock"]
                cantidad_compra += cantidad
            precio_producto = lista_de_productos[producto]["precio"]
            carrito_compras[producto]={ 
                        "precio": int(precio_producto),
                        "stock" :cantidad_compra
                        }
            return True
    else:
        print("\n Producto no encontrado... ")

def   calcular_total():
    precio = 0
    for producto, datos in carrito_compras.items():
        precio +=datos["precio"]
        tabla.append([producto, datos["precio"]])
    print(tabulate(tabla, headers=["Nombre", "Precio"], tablefmt="grid"))
    tabla.clear()


opcion = ""
primera_compra = True
limpiar_consola()

while opcion != "n":
    if primera_compra or opcion == "s":
        opcion=""
        primera_compra = False
        while True:
            listar_producto()
            nombre_producto= input("\n ¿Qué producto desea comprar?: ")
            cantidad_producto  =input("\n ¿Qué cantidad?:")
            if nombre_producto == '' or cantidad_producto == '' or int(cantidad_producto)<=0 :
                limpiar_consola()
            else :
                if not agregar_al_carrito(nombre_producto, int(cantidad_producto)):
                    limpiar_consola()
                    input(f"\n ¡No hay suficiente stock de {nombre_producto}! \n\t \nPresione ENTER...")
                    limpiar_consola()
                else:
                    break
    else:
        limpiar_consola()
        mostrar_carrito()
        opcion= input("\n ¿Desea continuar? s/n: ")
        limpiar_consola()


calcular_total()