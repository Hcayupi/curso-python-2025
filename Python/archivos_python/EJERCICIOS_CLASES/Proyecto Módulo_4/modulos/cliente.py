class Cliente:
    def __init__(
        self,
        id: int,
        nombre: str,
        apellido: str,
        email: str,
        telefono: str,
        direccion: str,
    ):
        self.__id = id
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__telefono = telefono
        self.__direccion = direccion

    def mostrar_info(self):
        return (
            f"- Nombre: {self.__nombre} {self.__apellido}\n"
            f"- Email: {self.__email}\n"
            f"- Teléfono: {self.__telefono}\n"
            f"- Dirección: {self.__direccion}"
        )

    def __str__(self):
        return f"- Nombre: {self.__nombre} {self.__apellido}\n"

    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_email(self):
        return self.__email

    def get_telefono(self):
        return self.__telefono

    def get_direccion(self):
        return self.__direccion

    def get_tipo(self):
        return self.__class__.__name__
