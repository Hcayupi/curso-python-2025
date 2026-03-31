from modulos.cliente import Cliente


class ClientePremium(Cliente):

    descuento = 0

    def __init__(
        self,
        id: int,
        nombre: str,
        apellido: str,
        email: str,
        telefono: str,
        direccion: str,
        descuento: float,
    ):

        super().__init__(id, nombre, apellido, email, telefono, direccion)
        self._descuento = descuento

    def mostrar_info(self):
        return (
            f"Cliente premium: {super().mostrar_info()}"
            f"\n- Descuento: {self._descuento}"
        )

    def get_descuento(self):
        return self._descuento
