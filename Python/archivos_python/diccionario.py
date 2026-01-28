#*Crear un diccionario
alumno = {
    "nombre": "Ana",
    "edad": 27,
    "ciudad": "Temuco"
}

#*Acceder 
print(alumno["nombre"])

#*Modificar
alumno["edad"] = 28 

#*Agregar nueva clave
alumno["curso"] = "Fundamentos de Python"
print(alumno)

print("nombre" in alumno)
print("direccion" not in alumno)


alumno = {
    "nombre": "Ana",
    "edad": 27,
    "ciudad": "Temuco"
}
direccion = alumno.get("direccion")#Devuelve por Default None cuando encuentra la key o no existe la key 

if direccion:
    print("La key existe")
else:
    print("La key no existe")


#Otro ejemplo
direccion = alumno.get("direccion", "La key no existe")
print(direccion)

alumno = {
    "nombre": "Ana",
    "edad": 27,
    "ciudad": "Temuco"
}
del alumno["ciudad"]
print(alumno)

#Otra alternativa
alumno.pop("edad")
print(alumno)


#* Ejemplos con con más de un elemento
alumnos = {
    "Ana":   {  
                "edad": 11, 
                "curso": "6°A", 
                "promedio": 6.2
            },
    "Luis":  {
                "edad": 12, 
                "curso": "6°A", 
                "promedio": 5.4
            },
    "Pedro": {"edad": 11, "curso": "6°B", "promedio": 6.8},
    "Sofía": {"edad": 12, "curso": "6°B", "promedio": 6.0}
}

#Acceder a un alumno
print(alumnos["Ana"])
print(alumnos.get("Pedro"))

#Acceder a un dato en especifíco
print(alumnos["Ana"]["curso"])
print(alumnos.get("Pedro").get("curso"))

#Modificar un dato
alumnos["Ana"]["curso"] = "6°B"

#Agregar un nuevo dato
alumnos["Ana"]["asistencia"] = 70
print(alumnos["Ana"])


print("======= Eliminar ========")
del alumnos["Camila"]
print(alumnos)
alumnos.pop("Camila")
print(alumnos)

#Buscar alumno (sin error)
nombre_buscar = "Camila"

if nombre_buscar in alumnos:
    alumnos.pop("Camila")
else:
    print(f"No existe alumno {nombre_buscar}")


#*Métodos importantes de diccionarios
productos = {
    "pan" : {"precio": 2000, "stock": 100},
    "leche" : {"precio": 1000, "stock": 35}
}

#*Alternativa al método get
try:
    print(productos["jugo"])
except:
    print("No existe el producto")

#*Recupera y si no existe lo crea
arroz = productos.setdefault("arroz", {"precio": 1990, "stock": 30})
print(productos)

pescado = productos.setdefault("pescado")
print(pescado)

#*Actualizar (con otro diccionario)
nuevos = {
    "pescado":  {"precio": 3500, "stock": 35},
    "huevos":  {"precio": 400, "stock": 35}
}

productos.update(nuevos)
print(productos)

#* Borrar todo el diccionario
productos.clear()
print(productos)   