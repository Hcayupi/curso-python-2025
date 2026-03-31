import csv
from modulos.gestor_cliente import GestorClientes
from modulos.cliente_regular import ClienteRegular
from modulos.cliente_premium import ClientePremium
from modulos.cliente_corporativo import ClienteCorporativo
from datetime import datetime


def exportar_clientes(clientes, ruta="datos/clientes.csv"):
    try:
        with open(ruta, "w", newline="", encoding="utf-8") as archivo:
            writer = csv.writer(archivo)

            writer.writerow(
                [
                    "id",
                    "nombre",
                    "apellido",
                    "email",
                    "telefono",
                    "direccion",
                    "tipo",
                    "descuento",
                    "empresa",
                ]
            )

            for cliente in clientes:
                descuento = ""
                empresa = ""

                if hasattr(cliente, "_descuento"):
                    descuento = cliente.get_descuento()

                if hasattr(cliente, "_empresa"):
                    empresa = cliente.get_empresa()

                writer.writerow(
                    [
                        cliente.get_id(),
                        cliente.get_nombre(),
                        cliente.get_apellido(),
                        cliente.get_email(),
                        cliente.get_telefono(),
                        cliente.get_direccion(),
                        cliente.get_tipo(),
                        descuento,
                        empresa,
                    ]
                )
    except FileNotFoundError:
        print("Archivo no encontrado.")
    except Exception as e:
        print(f"Error leyendo archivo: {e}")


TIPOS_CLIENTE = {
    "ClienteRegular": ClienteRegular,
    "ClientePremium": ClientePremium,
    "ClienteCorporativo": ClienteCorporativo,
}


def importar_clientes(ruta="datos/clientes.csv"):
    clientes = []

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            reader = csv.DictReader(archivo)

            for fila in reader:

                clase_cliente = TIPOS_CLIENTE.get(fila["tipo"])

                if not clase_cliente:
                    continue

                datos = [
                    int(fila["id"]),
                    fila["nombre"],
                    fila["apellido"],
                    fila["email"],
                    fila["telefono"],
                    fila["direccion"],
                ]

                if fila["tipo"] == "ClientePremium":
                    if fila["descuento"]:
                        datos.append(float(fila["descuento"]))
                    else:
                        datos.append(0.0)

                elif fila["tipo"] == "ClienteCorporativo":
                    datos.append(fila["empresa"])

                cliente = clase_cliente(*datos)
                clientes.append(cliente)

    except FileNotFoundError:
        print("Archivo no encontrado.")
    except Exception as e:
        print(f"Error leyendo archivo: {e}")

    return clientes


def generar_reporte(clientes, ruta="reportes/resumen.txt"):
    total = len(clientes)
    try:
        with open(ruta, "w", encoding="utf-8") as archivo:
            archivo.write("REPORTE DE CLIENTES\n")
            archivo.write("=" * 30 + "\n")
            archivo.write(f"Total clientes: {total}\n")
    except FileNotFoundError:
        print("Archivo no encontrado.")
    except Exception as e:
        print(f"Error leyendo archivo: {e}")


def registrar_log(mensaje, ruta="logs/app.log"):
    try:

        with open(ruta, "a", encoding="utf-8") as archivo:
            fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            archivo.write(f"[{fecha}] {mensaje}\n")

    except FileNotFoundError:
        print("Archivo no encontrado.")
    except Exception as e:
        print(f"Error leyendo archivo: {e}")
