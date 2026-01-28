"""
Demo de ENCAPSULAMIENTO:
El saldo se protege usando un atributo "privado" (__saldo) y solo
se puede modificar con métodos seguros.
"""


'''
Vamos a crear una clase que proteja el saldo del usuario 
y permita manipularlo solo mediante métodos seguros.

1. Definir clase CuentaBancaria con:
● Atributo privado __saldo
● Atributo público titular
● Atributo protegido _dirección
2. Crear métodos:
● depositar(monto): suma si el monto es válido
● retirar(monto): resta si hay suficiente saldo
● ver_saldo(): muestra el saldo actual
3. Mostrar que no se puede acceder a __saldo directamente
4. Usar los métodos para operar con seguridad
Objetivo: entender cómo proteger los datos internos del objeto y operar sobre ellos de forma
controlada.
'''

class CuentaBancaria:

    def __init__(self, titular, direccion, saldo=0):
        """
        Atributo protegido (convención)

        ¿Qué significa?
        -NO es una protección real
        -Es una señal para el desarrollador tenga cuidado 
        al manipular este atributo
        """
        self.titular = titular #publico
        self._direccion = direccion #protegido
        self.__saldo = saldo #privado
    
    def depositar(self,monto):
        if monto<=0:
            print("Monto inválido.Debe ser mayor a 0")
            return
        
        self.__saldo += monto
        print(f"Depósito realizado de manera correcta. Nuevo saldo: {self.__saldo}")
    
    def ver_saldo (self):
        print(f"Saldo actual es de: {self.__saldo}")

    

cuenta_uno = CuentaBancaria("Luis", "Avenida Siempreviva 742")

cuenta_uno.depositar(100000)

cuenta_uno.__saldo=350000

cuenta_uno.ver_saldo()