def listar_productos(productos):
    if not productos:
        return None
    return productos

def agregar_producto(productos, nuevo_producto, id_anexo):
    productos[id_anexo] = nuevo_producto
    

def buscar_producto_por_id(productos, id):
    producto = productos.get(id.upper())
    if not producto:
        return None
    return producto

def editar_producto(producto, nuevo_stock):
        producto["stock"] = nuevo_stock

def eliminar_producto(productos, id):
    producto = productos.get(id.upper())
    if producto:
        del productos[id.upper()]