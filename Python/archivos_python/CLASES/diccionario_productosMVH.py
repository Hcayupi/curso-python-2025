"""===============Diccionario anidado de productos======================
¿En qué consistirá la Demo?
Vamos a simular una base de datos de productos utilizando un diccionario anidado, donde cada producto tiene
un identificador único y contiene información como nombre, precio y stock.
1. Crear un diccionario productos donde cada clave sea un ID ("P001", "P002", etc.)
2. Cada valor será un diccionario con los campos: nombre, precio, stock
3. Acceder a los datos de un producto por su ID
4. Agregar un nuevo producto al diccionario
5. Modificar el stock de un producto existente
6. Eliminar un producto usando pop()
7. Iterar sobre todos los productos mostrando:
8. "Producto: Teclado | Precio: $5000 | Stock: 10"
9. Bonus: Mostrar solo los productos con stock menor a 10
"""

def printTituloLista():
    print("\nLista de productos\n")
    print("ID°    |  Nombre   |  Precio    |  Stock  |")

def listarProducto(index, datos):
    print(f"{index:<6}  {datos["nombre"]:<13}  {datos["precio"]:<8}   {datos["stock"]}") 

def listarProductoSimple(producto):
    print("\n|   Nombre  | Precio  |  Stock  ")
    print("    " , producto["nombre"] , "    " , producto["precio"] , "     " , producto["stock"])

diccionario_de_productos = {
    "P001": {"nombre": "Teclado", "precio": 5000, "stock": 10},
    "P002": {"nombre": "Mouse", "precio": 2500, "stock": 5},
    "P003": {"nombre": "Monitor", "precio": 15000, "stock": 2},
    "P004": {"nombre": "Hdmi", "precio": 5000, "stock": 7},
    "P005": {"nombre": "Ventilador", "precio": 15000, "stock": 3}
}   

opcion=0

while opcion!=7  :

    print("\nMenu")
    print("1) Buscar producto")
    print("2) Registrar nuevo producto")
    print("3) Modificar stock de producto")
    print("4) Eliminar producto")
    print("5) Listar productos")
    print("6) Productos con stock")
    print("7) Salir")

    opcion = int(input("Elige una opción: "))

    match opcion:
        case 1: 
                while True:
                    producto_id = input("\n Ingrese código de producto: ")
                    producto = diccionario_de_productos.get(producto_id.upper())
                    if producto:
                        listarProductoSimple(producto)
                        break
                    else:
                        print("\n El ID no existe...")
        case 2: 
                contador_producto = len(diccionario_de_productos)
                
                nombreProducto= input ("\n Ingrese nombre del producto: ")
                precioProducto = int(input("\n Ingrese precio del producto: "))
                stockProducto = int(input("\n Ingrese el stock del producto: "))

                contador_producto += 1

                diccionario_de_productos["P00"+ str(contador_producto)] = {
                    "nombre" : nombreProducto,
                    "precio" : precioProducto,
                    "stock"  : stockProducto
                }

                print("\n Producto registrado con exito...")
        case 3:
                producto_id = input("\n Ingrese código de producto: ")
                
                producto = diccionario_de_productos.get(producto_id.upper())

                if producto:
                    stockProducto = int(input("\n Ingrese el nuevo stock: "))
                    producto["stock"] = stockProducto
                    print("\n Stock modificado exitosamente...")
                    listarProductoSimple(producto)
                else:
                    print("\n Producto no encontrado...")
        case 4:
                producto_id = input("\n Ingrese código de producto: ")
                producto = diccionario_de_productos.get(producto_id.upper())

                if producto:
                    del diccionario_de_productos[producto_id.upper()]
                    print("\n Producto eliminado con exito...")
                else:
                    print("\n Producto no encontrado...")
        case 5: 
                printTituloLista()
                for index, datos in diccionario_de_productos.items():
                    listarProducto(index, datos)
        
        case 6: 
                printTituloLista()
                
                for index, datos in diccionario_de_productos.items():
                    if int(datos["stock"]) < 10:
                        listarProducto(index, datos)
        
