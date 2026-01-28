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
