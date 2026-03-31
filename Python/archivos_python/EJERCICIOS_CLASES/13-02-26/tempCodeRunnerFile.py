def validar_email(email):
    if "@" not in email:
        raise ValueError("email inválido")
    
def regitrar_usuario(email):
    try:
        validar_email(email)
    except ValueError as e:
        print("Error interno: ", e)

try:
    regitrar_usuario("usuario_sin_arroba.com")
except ValueError:
    print("Error detectado en el sistema externo: reintenta con un email válido")