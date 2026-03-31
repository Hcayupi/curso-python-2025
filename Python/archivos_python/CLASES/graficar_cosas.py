from tabulate import tabulate

alumnos = {
    "Ana" : 6.5,
    "Juan": 5.8,
    "Pedro": 4.5
}

tabla = []

for nombre, nota in alumnos.items():
    tabla.append([nombre, nota])

print(tabulate(tabla, headers=["Alumno", "Nota"], tablefmt="grid"))


from rich.console import Console
from rich.table import Table

datos = {"Pan": 12, "Leche": 5, "Huevos": 20}
maxv = max(datos.values())

table = Table(title="Stock (barras)")
table.add_column("Producto")
table.add_column("Cantidad")
table.add_column("Barra")

for k, v in datos.items():
    barra = "█" * int((v / maxv) * 20)
    table.add_row(k, str(v), barra)

Console().print(table)