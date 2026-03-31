'''
Modelá una jerarquía de transporte
Contexto:
Queremos modelar un animal con habilidades combinadas.
Consigna:
Definí las siguientes clases:
● Volador: método moverse() imprime "Estoy volando"
● Nadador: método moverse() imprime "Estoy
nadando"
● Pato: hereda de ambas clases, no sobrescribe
moverse()

Paso a paso:
1. Creá un objeto Pato y llamá a moverse()
2. Usá Pato.__mro__ o help(Pato) para
mostrar el orden de resolución
3. Cambiá el orden de herencia y volvé a
probar
4. Agregá un método propio en Pato que
combine ambos comportamientos
'''

class Volador:
    def moverse(self):
        print("Estoy volando")

class Nadador:
    def moverse(self):
        print("Estoy nadando")

class Pato(Nadador, Volador):
    pass

pato = Pato()

pato.moverse()

print(help(Pato))