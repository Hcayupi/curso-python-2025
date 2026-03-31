from modulos.cliente import Cliente


class ClienteCorporativo(Cliente):

    def __init__(
        self,
        id: int,
        nombre: str,
        apellido: str,
        email: str,
        telefono: str,
        direccion: str,
        empresa: str,
    ):
        super().__init__(id, nombre, apellido, email, telefono, direccion)
        self._empresa = empresa

    def mostrar_info(self):
        return (
            f"Cliente corporativo: {super().mostrar_info()} "
            f"\n- Empresa: {self._empresa}"
        )

    def get_empresa(self):
        return self._empresa
