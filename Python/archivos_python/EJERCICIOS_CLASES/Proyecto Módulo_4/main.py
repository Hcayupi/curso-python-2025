from modulos.gestor_cliente import GestorClientes
from modulos.cliente_regular import ClienteRegular
from modulos.cliente_premium import ClientePremium
from modulos.cliente_corporativo import ClienteCorporativo
from modulos.archivos import (
    exportar_clientes,
    generar_reporte,
    registrar_log,
    importar_clientes,
)

gestor = GestorClientes(guardar_callback=exportar_clientes)
clientes_importados = importar_clientes()
gestor.cargar_clientes(clientes_importados)


def info_guardado():
    print("\n Cliente guardado con exito...")
    registrar_log("Cliente agregado")


while True:

    print("\n===== GESTOR DE CLIENTES =====")
    print("1. Agregar cliente")
    print("2. Listar clientes")
    print("3. Buscar cliente")
    print("4. Eliminar cliente")
    print("5. Generar reporte")
    print("6. Salir")

    try:
        opcion = int(input("Seleccione opción: "))
        match opcion:
            case 1:
                print("\nTipo de cliente:")
                print("1. Regular")
                print("2. Premium")
                print("3. Corporativo")
                try:
                    tipo = int(input("Seleccione tipo: "))

                    id = int(input("ID: "))
                    nombre = input("Nombre: ")
                    apellido = input("Apellido: ")
                    email = input("Email: ")
                    telefono = input("Telefono: ")
                    direccion = input("Direccion: ")

                    match tipo:
                        case 1:
                            cliente = ClienteRegular(
                                id, nombre, apellido, email, telefono, direccion
                            )
                            gestor.agregar_cliente(cliente)
                            info_guardado()
                        case 2:
                            try:
                                descuento = float(input("Descuento (%): "))
                                cliente = ClientePremium(
                                    id,
                                    nombre,
                                    apellido,
                                    email,
                                    telefono,
                                    direccion,
                                    descuento,
                                )
                                gestor.agregar_cliente(cliente)
                                info_guardado()
                            except ValueError:
                                print("\n Ingrese un descuento válido")
                        case 3:
                            empresa = input("Empresa: ")
                            cliente = ClienteCorporativo(
                                id,
                                nombre,
                                apellido,
                                email,
                                telefono,
                                direccion,
                                empresa,
                            )
                            gestor.agregar_cliente(cliente)
                            info_guardado()

                        case 4:
                            None
                except ValueError:
                    print("\nDebe ingresar un número válido")
                    continue

            case 2:
                print("\n", gestor.listar_clientes())

            case 3:
                try:
                    id = int(input("ID a buscar: "))
                    cliente = gestor.buscar_cliente(id)
                    print()
                    if cliente:
                        print(cliente.mostrar_info())
                    else:
                        print("Cliente no encontrado")
                except ValueError:
                    print("\nDebe ingresar un número válido")
                continue

            case 4:
                try:
                    id_cliente = int(input("ID: "))

                    print()
                    if gestor.eliminar_cliente(id):
                        print("Cliente eliminado")
                        registrar_log("Cliente eliminado")
                    else:
                        print("No existe el cliente")

                except ValueError:
                    print("\nDebe ingresar un número válido")
                continue
            case 5:
                generar_reporte(gestor.get_clientes())

            case 6:
                print("Saliendo...")
                break
    except ValueError:
        print("\nDebe ingresar un número válido")
        continue
