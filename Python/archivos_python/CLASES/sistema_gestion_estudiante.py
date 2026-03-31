"""Contexto:
Una institución educativa necesita registrar y consultar información de sus estudiantes. Cada estudiante
tiene un nombre, una edad y una ciudad de residencia. Se requiere un sistema básico para almacenar los
datos, listarlos, buscar estudiantes por ciudad y obtener estadísticas.
Consigna:

● Desarrollar un programa que permita:
● Registrar múltiples estudiantes representados por tuplas dentro de una lista.
● Mostrar todos los registros con formato legible.
● Permitir consultar cuántos estudiantes son de una ciudad específica.
● Mostrar la edad promedio de los estudiantes registrados."""

estudiante=[
    ("Ana", 18, "Temuco"),
    ("Luis", 21, "Santiago"),
    ("María", 19, "Temuco"),
    ("Pedro", 22, "Valdivia"),
    ("Carla", 20, "Santiago"),
    ("Diego", 23, "Temuco")
]

opcion=0

while opcion!=8  :

    print("\nMenu")
    print("1) Registrar estudiante")
    print("2) Listar estudiantes")
    print("3) Buscar estudiante por ciudad")
    print("4) Estudiantes por ciudad")
    print("5) Promedio de edad de estudiantes")
    print("6) Modificar alumno")
    print("7) Eliminar alumno")
    print("8) Salir")

    opcion = int(input("Elige una opción: "))

    match opcion:
        case 1: 
            nombre=input("Nombre estudiante: ")
            edad = int(input("Edad: "))
            ciudad=input("Ciudad: ")

            estudiante.append((nombre, edad, ciudad))
        case 2: 
            for nombre, edad, ciudad in estudiante:
                print(f"\nNombre: {nombre}. Edad: {edad}. Ciudad: {ciudad}")
        case 3: 
            buscaCiudad = input("\nIngrese ciudad: ")

            for nombre, edad, ciudad in estudiante:
                if ciudad.lower()==buscaCiudad.lower():
                    print(f"\nNombre: {nombre} Edad:{edad} Ciudad: {ciudad}")   
        case 4:
            contador = 0
            ciudadEstudiante = input("\nIngrese la ciudad a consultar: ")
            for nombre, edad, ciudad in estudiante:
                    if ciudad.lower()==ciudadEstudiante.lower():
                        contador+=1
            
            print(f"\nHay {contador} estudiantes en la ciudad de {ciudadEstudiante}")

        case 5:
            sumaEdad = 0
            for nombre, edad, ciudad in estudiante:
                    sumaEdad +=int(edad)
            promedioEdad = sumaEdad /len(estudiante)

            print(f"\nPromedio edad de todos los estudiantes:{promedioEdad}")
        
        case 6:
            contador = 0
            nombreEstudianteModificar = input("\nIngrese nombre del estudiante a modificar: ")
            print("\nLista de estudiantes\n")
            print("N°    |  Nombre   |  Edad    |  Ciudad  |")
            for index,(nombre, edad, ciudad) in enumerate(estudiante):
                 if nombreEstudianteModificar.lower() == nombre.lower():
                    print(f"  \n{index}   -       {nombre}        {edad}       {ciudad}")
                    contador+=1
            
            print(f"\n Se han encontrado {contador} coincidencia(s)")

            indexModificar = int(input("\n¿Qué regitro desea modificar? \nIngrese número de regitro: "))

            for index,(nombre, edad, ciudad) in enumerate(estudiante):
                if indexModificar==index:
                    nombre = input("\nNombre: ")
                    edad = input("\nEdad: ")
                    ciudad = input("\nCiudad: ")
                    estudiante[index]=(nombre, edad, ciudad)

            print("\n Modificación realizada...")
        case 7:
            contador = 0
            nombreEstudianteModificar = input("Ingrese nombre del estudiante a eliminar: ")
            print("\nLista de estudiantes\n")
            print("N°    |  Nombre   |  Edad    |  Ciudad  |")
            for index,(nombre, edad, ciudad) in enumerate(estudiante):
                 if nombreEstudianteModificar.lower() == nombre.lower():
                    print(f"  \n{index}   -       {nombre}        {edad}       {ciudad}")
                    contador+=1
            
            print(f"\n Se han encontrado {contador} coincidencia(s)")

            indexModificar = int(input("\n¿Qué regitro desea eliminar? \nIngrese número de regitro: "))

            for index,(nombre, edad, ciudad) in enumerate(estudiante):
                if indexModificar==index:
                    estudiante.pop(index)
            print("\n Registro eliminado exitosamente...")

        case _:
            print("\nNo es una opción válida\n")                       
