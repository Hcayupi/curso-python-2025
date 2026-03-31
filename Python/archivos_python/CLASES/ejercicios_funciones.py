'''
1) Agenda: guardar y buscar teléfonos

Enunciado:
Crea un diccionario agenda donde la clave es el nombre y el valor es el teléfono.

Crea una función guardar_contacto(agenda, nombre, telefono) que guarde/actualice el contacto.

Crea una función buscar_contacto(agenda, nombre) que devuelva el teléfono si existe, o "No encontrado" si no existe.

Prueba guardando 3 contactos y luego buscando uno.
'''
diccionario_contactos = {
    "pedro":{"telefono":555}
    }

def guardar_contacto(nombre, telefono):

    if nombre in diccionario_contactos:
        diccionario_contactos[nombre]["telefono"]=telefono
        print("ACTUALIZADO" , diccionario_contactos) 
    else:
        diccionario_contactos[nombre]={"telefono": telefono}  
        print("NUEVO", diccionario_contactos) 

    


def buscar_contacto(nombre):
    if nombre in diccionario_contactos:
        return diccionario_contactos[nombre]["telefono"]
    else:
        print("\n No encontrado")

opcion=0

while opcion!=3  :
    print("\nMenu")
    print("1) Registrar contacto")
    print("2) Buscar contacto")
    print("3) Salir")

    opcion = int(input("Elige una opción: "))

    match opcion:
        case 1:     
            nombre_contacto = input("\n Nombre: ")
            telefono_contacto = int(input("\n Teléfono: "))
            guardar_contacto(nombre_contacto, telefono_contacto)
        case 2: 
            nombre_contacto = input("\n Nombre: ")
            print(buscar_contacto(nombre_contacto))


'''
2) “Mini-buscador” de productos por ID (diccionario anidado)

Enunciado:
Tienes productos guardados por ID. Pide al usuario un ID y muestra el producto.
Si no existe, muestra “No encontrado”.

'''

diccionario_productos = {
    "P001": {"nombre": "pan", "precio": 500},
    "P002": {"nombre": "leche", "precio": 900},
    "P003": {"nombre": "manzana", "precio": 300},
    "P004": {"nombre": "arroz", "precio": 1800},
    "P005": {"nombre": "fideos", "precio": 1100},
    "P006": {"nombre": "aceite", "precio": 3500}
}

def buscar_contacto(id_producto):
    if id_producto in diccionario_productos:
        nombre_producto = diccionario_productos[id_producto]["nombre"]
        precio_producto = str(diccionario_productos[id_producto]["precio"])
        print(f"Nombre: {nombre_producto}, Precio: {precio_producto}" )
    else:
        print("\n No encontrado...")

buscar_contacto("P005")

'''
3) Actualizar stock con validación

Enunciado:
Tienes este stock. Pide un producto y cuántas unidades se venden.

Si el producto no existe → avisa.
Si no hay stock suficiente → avisa.
Si se puede → descuenta y muestra el stock final.
'''
lista_de_productos = {
    "manzana": {"precio": 500,"cantidad": 4 },
    "pan": {"precio": 1200,"cantidad": 2},
    "leche": {"precio": 900,"cantidad": 1},
    "arroz": {"precio": 1800,"cantidad": 2},
    "fideos": {"precio": 1100,"cantidad": 3},
    "aceite": {"precio": 3500,"cantidad": 1},
    "azúcar": {"precio": 1300,"cantidad": 2},
    "sal": {"precio": 600,"cantidad": 1},
    "huevos": {"precio": 4200,"cantidad": 0},
    "queso": {"precio": 5500,"cantidad": 1}
}

def buscar_productos(nombre_producto):
    if nombre_producto in lista_de_productos:
        precio_producto = lista_de_productos[nombre_producto]["precio"]
        stock_producto = lista_de_productos[nombre_producto]["cantidad"]
        if stock_producto == 0:
            print(f"\n No hay stock de {nombre_producto}\n")
            return False
        else:
            print(f"\nNombre: {nombre_producto}, Precio: {precio_producto}, Stock: {stock_producto}\n")
            return True
    else:
        print("\n Producto no encontrado...\n")
        return False

def comprar_producto(nombre_producto):
    if nombre_producto in lista_de_productos:
        precio_producto = lista_de_productos[nombre_producto]["precio"]
        stock_producto = lista_de_productos[nombre_producto]["cantidad"]
        stock_producto -=1
        lista_de_productos[nombre_producto]["cantidad"]= stock_producto
        print(f"\nNombre: {nombre_producto}, Precio: {precio_producto}, Stock: {stock_producto}\n ")


while True:
    ingreso_usuario = input("\n ¿Qué producto desea consultar?: ")

    if buscar_productos(ingreso_usuario):
        opcion_compra = input("\n ¿Desea comprarlo? s/n: ")
        if opcion_compra == "s":
            comprar_producto(ingreso_usuario)
        elif opcion_compra =="n":
            break 



'''
4) Contar letras de una frase (ignorando espacios)

Enunciado:
Pide una frase al usuario y crea un diccionario con cuántas veces aparece cada letra.
Ignora los espacios y cuenta todo en minúscula.

Ejemplo: "Hola hola" → {'h':2,'o':2,'l':2,'a':2}
'''

diccionario_letras={}

def contar_letras(frase):
    diccionario_letras[frase]={}
    for letra in frase:
        if letra!= " ":
            if letra in diccionario_letras[frase]:  
                diccionario_letras[frase][letra]+=1 
            else:
                diccionario_letras[frase][letra]=1

def listar_diccionario_frases():

    for clave, datos in diccionario_letras.items():
        print(f"- {clave} , {datos} ")

while True:

    frase_usuario = input("\n + Ingrese una frase o presione ENTER: ")
    
    if frase_usuario == "" : 
        break

    contar_letras(frase_usuario)
    print("\n")
    listar_diccionario_frases()


'''
5) Diccionario de alumnos: buscar mejor/peor nota

Enunciado:
Tienes este diccionario de alumnos y sus notas.
Debes mostrar:

El alumno con mejor nota
El alumno con peor nota
El promedio del curso
'''

diccionario_notas={
    "Ana": [6.5, 5.8, 6.2],
    "Luis": [4.9, 5.1, 5.5],
    "Pedro": [6.0, 6.7, 6.4],
    "Sofía": [5.5, 5.9, 6.1]
}

diccionario_ranking={}

def listar_notas():
    for clave, datos in diccionario_notas.items():
        print(f" { clave } - {datos}")

def ranquear_notas(): 
    nota_mayor = 0.0 
    nota_menor = None
    for clave, datos in diccionario_notas.items():
        nota_mayor = 0.0 
        for notas in datos:
            if not nota_menor:
                nota_menor = notas
            if notas>nota_mayor:
                nota_mayor = notas  
            
            if nota_menor<notas:
                nota_menor=notas
                
    diccionario_ranking[clave]=nota_mayor 
    
    print(f"\n- Peor nota : {nota_menor}")

def analiza_ranking():
    nota_mayor = 0.0 
    nota_menor = 0.0
    alumno_mayor = ""
    alumno_menor = ""
    for clave, nota in diccionario_ranking.items():
        if nota>nota_mayor:
            nota_mayor = nota
            alumno_mayor = clave
        else:
            nota_menor=nota
            alumno_menor=clave            

    print(f" - Mejor nota=  {alumno_mayor} : {nota_mayor}")
listar_notas()
ranquear_notas()
analiza_ranking()


