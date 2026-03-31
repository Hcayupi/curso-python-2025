from modulos.cliente import Cliente


class ClienteRegular(Cliente):

    def mostrar_info(self):
        return f"Cliente regular:  {super().mostrar_info()}"
