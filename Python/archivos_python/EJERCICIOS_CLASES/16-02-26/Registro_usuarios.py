'''
Registro de usuario con validaciones y errores personalizados
Contexto:
Estás desarrollando el sistema de registro de una aplicación. 
Necesitás validar datos de entrada del usuario y manejar errores 
de forma estructurada y segura.
Consigna:
Implementá un programa que:
Solicite al usuario que ingrese su nombre, edad y email
Valide:
● Que el nombre no esté vacío
● Que la edad sea mayor a 0
● Que el email contenga @
Lance excepciones personalizadas en cada caso de error
Organice los errores en una jerarquía con una clase base
Use try/except para capturar y diferenciar errores
Utilice un bloque finally para mostrar un mensaje final de
cierre
'''

class ErrorRegistro(Exception):
    pass


class NombreInvalidoError(ErrorRegistro):
    pass


class EdadInvalidaError(ErrorRegistro):
    pass


class EmailInvalidoError(ErrorRegistro):
    pass


def validar_nombre(nombre):
    if nombre.strip() == "":
        raise NombreInvalidoError("<< Nombre no puede ir vacio >>")


def validar_edad(edad):
    if edad <= 0:
        raise EdadInvalidaError("<< La edad no puede ser negativa >>")


def validar_email(email):
    if "@" not in email:
        raise EmailInvalidoError("<< Email inválido >>")

while True:
    try:

        nombre = input("Ingrese su nombre : ")
        edad = int(input("Ingrese su edad : "))
        email = input("Ingrese su email : ")
        print()
        validar_nombre(nombre)
        validar_edad(edad)
        validar_email(email)
        break
    except NombreInvalidoError as e:
        print(e)
    except EdadInvalidaError as e:
        print(e)
    except EmailInvalidoError as e:
        print(e)
    except ValueError:
        print("<< La edad debe ser un numero entero >>")
    finally:
        print()
        print("Cerrando proceso de registro...")
        print()