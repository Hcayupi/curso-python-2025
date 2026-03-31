CREATE TABLE categorias(
	id_categoria SERIAL NOT NULL PRIMARY KEY,
	nombre_categoria VARCHAR(255),
	descripcion VARCHAR(255)
);

CREATE TABLE clientes (
	id_cliente SERIAL NOT NULL PRIMARY KEY,
	nombre_cliente VARCHAR(50),
	nombre_contacto VARCHAR(50),
	direccion VARCHAR(60),
	ciudad VARCHAR (30),
	codigo_postal VARCHAR(20),
	pais VARCHAR (20)	
);

CREATE TABLE productos(
	id_producto SERIAL NOT NULL PRIMARY KEY,
	nombre_producto VARCHAR (255),
	id_categoria INT NOT NULL REFERENCES categorias(id_categoria),
	unidad VARCHAR (50),
	precio DOUBLE PRECISION
);


CREATE TABLE pedidos(
	id_pedido SERIAL NOT NULL PRIMARY KEY,
	id_cliente INT NOT NULL REFERENCES clientes(id_cliente),
	fecha_pedido TIMESTAMPTZ NOT NULL DEFAULT now()
);


CREATE TABLE detalle_pedidos(
	id_detalle_pedido SERIAL NOT NULL PRIMARY KEY,
	id_pedido INT NOT NULL REFERENCES pedidos(id_pedido),
	id_producto INT NOT NULL REFERENCES productos(id_producto),
	cantidad INT NOT NULL
);

CREATE TABLE prueba_productos(
	id_prueba_productos SERIAL NOT NULL PRIMARY KEY,
	nombre_producto VARCHAR(60) NOT NULL,
	id_categoria INT NOT NULL REFERENCES categoria(id_categoria)
)


















