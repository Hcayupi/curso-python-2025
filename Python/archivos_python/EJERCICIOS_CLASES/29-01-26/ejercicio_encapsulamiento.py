"""
Diseñá una clase DispositivoInteligente

Contexto:
Queremos representar un dispositivo como un objeto que puede encenderse, conectarse a WiFi y mostrar su
estado, ocultando los detalles técnicos al usuario.
Consigna:
● Creá una clase DispositivoInteligente con:
● Atributos privados: __encendido,
__conectado
● Atributo público: modelo
● Método encender() → cambia __encendido a
True
● Método conectar() → cambia __conectado a
True solo si está encendido
● Método estado() → devuelve "Conectado" o
"Desconectado" según su estado
Tiempo : 25 Minutos

Requisitos:
1. Encapsular el estado interno del
dispositivo
2. Evitar acceso directo a __encendido o
__conectado
3. Probar con dos dispositivos distintos
"""

class DispositivoInteligente:
        
    def __init__(self,nombre,modelo,encendido=False, contectado=False):
        self.nombre = nombre
        self.modelo = modelo
        self.__encendido = encendido
        self.__conectado = contectado

    def encender(self):
        if not self.__encendido:
            self.__encendido=True 
            print(f"+El dispositivo {self.nombre}, modelo {self.modelo} se ha encendido con éxito...")

    def conectar(self):
        if not self.__encendido:
            print(f"+El dispositivo {self.nombre}  no está encendido...")
            return
        self.__conectado=True

    def estado(self):
        if not self.__encendido:
            print(f"+El dispositivo {self.nombre} no está encendido...")
        elif not self.__conectado:
            print(f"+El dispositivo {self.nombre} no está conectado")
        else:
            print(f"+El dispositivo {self.nombre} está conectado")


dispositivo_uno = DispositivoInteligente("IA Home", "Huawei")
dispositivo_dos = DispositivoInteligente("Verisure", "001")

print(" ---- TEST de accesibilidad a atributo privado")

print(f"Dispositivo: {dispositivo_uno.nombre}")
dispositivo_uno.__encendido=True
dispositivo_uno.__conectado=True
dispositivo_uno.estado()

print(f"Dispositivo: {dispositivo_dos.nombre}")
dispositivo_dos.__encendido=True
dispositivo_dos.__conectado=True
dispositivo_dos.estado()
print("="* 30)

print("\n ---- TEST Encendidos de dispositivos")

print(f"Dispositivo: {dispositivo_uno.nombre}")
dispositivo_uno.encender()
print(f"Dispositivo: {dispositivo_dos.nombre}")
dispositivo_dos.encender()

print("\n ---- TEST de conexión a WIFI")
print(f"Dispositivo: {dispositivo_uno.nombre}")
dispositivo_uno.conectar()
dispositivo_uno.estado()
print(f"Dispositivo: {dispositivo_dos.nombre}")
dispositivo_dos.conectar()
dispositivo_dos.estado()

"""
Clase Empleado con control de salario

Contexto:
Necesitamos una clase que represente a un empleado con control total sobre el acceso y modificación del
salario, evitando errores y manteniendo la lógica protegida.
Consigna:
Creá una clase Empleado con:
● Atributos: nombre (público) y __salario
(privado)
● Método ver_salario()
● Método modificar_salario(nuevo_salario) con
validación (nuevo_salario > 0)
● Método mostrar_info() que imprima nombre y
salario

Tiempo : 20 Minutos

Requisitos:
1. No permitir modificar el salario
directamente desde fuera
2. Probar qué ocurre si se intenta hacer
empleado.__salario = -1000
3. Crear al menos 2 objetos con distintos
salarios y mostrar sus datos
"""

class Empleado:
    def __init__(self, nombre, salario=0):
        self.nombre = nombre
        self.__salario = salario

    def ver_salario(self):
        return self.__salario
    
    def modificar_salario (self, nuevo_salario):
        if nuevo_salario <=0:
            print("+El ingreso del salario debe ser mayor a cero")
            return
        self.__salario=nuevo_salario
    
    def mostrar_info(self):
        print(f"+Empleado {self.nombre} tiene un salario actual de {self.__salario}")


empleado_uno = Empleado("Juanito", 500)
empleado_dos = Empleado("Luly", 800)

print(" - TEST de acceso a atributos privados")
print(f"Se modifica salario de {empleado_uno.nombre} a 650 pesos")
empleado_uno.__salario=650
empleado_uno.mostrar_info()
print(f"\nSe modifica salario de {empleado_dos.nombre} a -1000 pesos")
empleado_dos.__salario=-1000
empleado_dos.mostrar_info()
print("="* 30)

print("\n - TEST de modificación a través de los métodos")
print(f"Se modifica salario de {empleado_uno.nombre} a 650 pesos")
empleado_uno.modificar_salario(650)
empleado_uno.mostrar_info()
print(f"\nSe modifica salario de {empleado_dos.nombre} a -1000 pesos")
empleado_dos.modificar_salario(-1000)
empleado_dos.mostrar_info()