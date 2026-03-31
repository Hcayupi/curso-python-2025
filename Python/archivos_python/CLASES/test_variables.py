def alumno_aprobado(resultado):
    if resultado:
        return "Aprobado"
    else: return "Reprobado"


def lista_asignaturas():
    print("\nIndique asignatura:")
    print("1.- Matemáticas")
    print("2.- Lenguaje")
    print("3.- Ciencias")
    return int(input("\nSeleccione asignatura: "))

def seleccion_asigntura(opcion):
    match opcion:
        case 1: return "Matemáticas"
        case 2: return "Lengueje"
        case 3: return "Ciencias"
        case _: return None

alumnos = {}
aprobado =False
numeros_alumnos=int(input("Total de alumnos: "))

for i in range(numeros_alumnos):
    nombre= input("\n\nIngrese nombre: ")
    edad = input("Ingrese edad del alumno: ")
        
    opcion = lista_asignaturas()

    asignatura = seleccion_asigntura(opcion)

    nota_asignatura=input("\nIngrese nota de la asignatura : ")

    if float(nota_asignatura)< 4.0:
        aprobado= False
    else: aprobado=True

    alumnos[nombre]={
        "edad": edad,
        "asignatura" : asignatura,
        "nota": nota_asignatura,
        "aprobado":aprobado
    }

print("\nLISTA DE ALUMNOS\n")

for nombre, dato in alumnos.items():
    print(nombre," | ", dato["edad"]," | ",dato["asignatura"]," | ",dato["nota"]," | ", alumno_aprobado(dato["aprobado"]), " | ")

#  ---- SUMA Y PROMEDIO DE NOTAS  ----

suma_de_notas = 0

for nombre, dato in alumnos.items():
    suma_de_notas = suma_de_notas + float(dato["nota"])

print(f"Promedio de notas del curso:{ float(suma_de_notas/len(alumnos))}")

