from app.controllers import productos as functions_productos
from app.utils import helpers as functions_helpers
from app.utils.helpers import imprimir_tabla
from colorama import Fore

def generar_menu(opciones):
    for i,opcion in enumerate(opciones):
        if i == 0:
            print(Fore.CYAN)
            print("\n" + "=" * 30)
            print(Fore.CYAN + "  " + opcion)
            print("=" * 30)
        else:
            print(Fore.GREEN + opcion)

    print("=" * 30)

def generar_tabla(datos):
    headers = ["ID", "nombre", "descripcion", "precio", "stock"]
    imprimir_tabla(datos, headers=headers, formato="double_outline")

def generar_id(datos):
    contador_producto = len(datos)
    contador_producto += 1
    return "P00"+ str(contador_producto)

def ejecutar_menu(productos,opciones_menu):
    functions_helpers.limpiar_consola()
    while True:
        generar_menu(opciones_menu)
        opcion = functions_helpers.leer_int("Elige una opción: ", minimo=0, maximo=6)
        print("\n")

        match opcion:
            case 1:
                productos = functions_productos.listar_productos(productos)
                if productos:
                    generar_tabla(productos)
                else:
                    functions_helpers.sin_datos() 
                functions_helpers.pausa()
                functions_helpers.limpiar_consola()

            case 2:
                nombre_producto= input ("\n Ingrese nombre del producto: ")
                descripcion_producto= input ("\n Ingrese descripcion del producto: ")
                precio_producto = int(input("\n Ingrese precio del producto: "))
                stock_producto = int(input("\n Ingrese el stock del producto: "))

                id_anexo = generar_id(productos)

                nuevo_producto= {
                    "nombre" : nombre_producto,
                    "descripcion": descripcion_producto,
                    "precio" : precio_producto,
                    "stock"  : stock_producto
                }

                functions_productos.agregar_producto(productos, nuevo_producto, id_anexo)
                functions_helpers.pausa()
                functions_helpers.limpiar_consola()

            case 3:
                producto_id = input("\n Ingrese código de producto: ")
                producto = functions_productos.buscar_producto_por_id(productos, producto_id.lower())
                if producto:
                    generar_tabla(producto)
                functions_helpers.pausa()
                functions_helpers.limpiar_consola()

            case 4:
                producto_id = input("\n Ingrese código de producto: ")
                producto = functions_productos.buscar_producto_por_id(productos, producto_id.lower())
                
                if producto:
                    stock_producto = int(input("\n Ingrese el nuevo stock: "))
                    functions_productos.editar_producto(producto,stock_producto)
                    functions_helpers.mensaje_orden_exitosa()
                else:
                    functions_helpers.mensaje_no_encontrado()
                        
                functions_helpers.pausa()
                functions_helpers.limpiar_consola()

            case 5:
                producto_id = input("\n Ingrese código de producto: ")
                functions_productos.eliminar_producto(productos, producto_id)
                functions_helpers.pausa()
                functions_helpers.limpiar_consola()

            #case 6 : GENERAR VENTA
            case 6:
                print("Saliendo del sistema...")
                break
