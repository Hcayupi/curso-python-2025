CREATE TABLE roles(
id_rol SERIAL NOT NULL PRIMARY KEY,
nombre VARCHAR(50) NOT NULL UNIQUE,
created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);


CREATE TABLE usuarios( 
id_usuario SERIAL NOT NULL PRIMARY KEY,
nombre VARCHAR(150) NOT NULL,
email VARCHAR(255) NOT NULL UNIQUE,
password VARCHAR(8) NOT NULL,
id_rol INT NOT NULL REFERENCES roles(id_rol),
created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

INSERT INTO roles (nombre) VALUES('Admin'), ('Cliente');
	
INSERT INTO usuarios (nombre, email, password, id_rol)
VALUES ('Ana', 'ana.contacto@gmail.com', '1234', 1)