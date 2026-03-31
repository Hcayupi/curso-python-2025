class GestorClientes:

    def __init__(self, guardar_callback=None):
        self.__clientes = []
        self._guardar = guardar_callback

    def agregar_cliente(self, cliente):
        self.__clientes.append(cliente)
        self._guardar_cambios()

    def listar_clientes(self):
        lista_clientes = ""
        for cliente in self.__clientes:
            lista_clientes += cliente.mostrar_info() + "\n"
            lista_clientes += "-" * 30 + "\n"
        return lista_clientes

    def buscar_cliente(self, id_cliente):
        for cliente in self.__clientes:
            if cliente.get_id() == id_cliente:
                return cliente

        return None

    def eliminar_cliente(self, id_cliente):
        cliente = self.buscar_cliente(id_cliente)

        if cliente:
            self.__clientes.remove(cliente)
            self._guardar_cambios()
            return True

        return False

    def get_clientes(self):
        return self.__clientes

    def _guardar_cambios(self):
        if self._guardar:
            self._guardar(self.__clientes)

    def cargar_clientes(self, lista_clientes):
        for cliente in lista_clientes:
            self.__clientes.append(cliente)
