#========================== LISTAS --->List ======================Ricardo Vega

alumnos = ["Ana", "Luis", "Pedro", "Sofía"]

print(alumnos[1])#Luis
print(alumnos[2])#Pedro
print(alumnos[3])#Sofía

#? Indices negativos
print(alumnos[-1])#Sofía
print(alumnos[-2])#Pedro

alumnos = ["Ana", "Luis", "Pedro", "Sofía"]

print(alumnos[1])#Luis
print(alumnos[2])#Pedro
print(alumnos[3])#Sofía

#? Indices negativos
print(alumnos[-1])#Sofía
print(alumnos[-2])#Pedro

#* ==== Modificación de una lista ====
#? Cambiar valor
alumnos[2] = "Lucas"
print(alumnos)

#? Agregar elementos
alumnos.append("Camila")#agregar al final de la lista
print(alumnos)

alumnos.insert(2, "Mateo")#agregar en una posición especifica
print(alumnos)

#? Eliminar elementos
alumnos.pop() #elimina el último
print(alumnos) 

#? Eliminar un el elemento por valor
alumnos.remove("Luis")#Elimina por valor
print(alumnos) 

#? Eliminar por el índice
alumnos.pop(2)
print(alumnos)


alumnos = ["Ana", "Luis", "Pedro", "Sofía"]
for indice, nombre in enumerate(alumnos, start=37):
    print(f"{indice} - {nombre}") 

#con while

indice = 0 #indice inicial

while indice < len(alumnos):
    print(f"{indice} - {nombre}")
    indice += 1
    
    
    
    alumnos = ["Ana", "Luis", "Pedro", "Sofía"]
for indice, nombre in enumerate(alumnos, start=37):
    print(f"{indice} - {nombre}") 

#con while

indice = 0 #indice inicial

while indice < len(alumnos):
    print(f"{indice} - {alumnos[indice]}")
    indice += 1 #!IMPORTANTE: avanzar para no quedar en un bucle infinito #!IMPORTANTE: avanzar para no quedar en un bucle infinito