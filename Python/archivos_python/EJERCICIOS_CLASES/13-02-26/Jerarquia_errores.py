class ErrorApplicacion(Exception):
    pass
class ErrorValidacion(ErrorApplicacion):
    pass
class ErrorPermisos(ErrorApplicacion):
    def __init__(self, mensaje, rol, codigo_error=403):
        super().__init__(mensaje)
        self.rol = rol
        self.codigo=codigo_error
    
    def detalle(self):
        return f"[{self.codigo}] '{ self.rol}' --->{self}"


def verificar_usuario(rol):
    if rol == "visitante":
        raise ErrorPermisos("Acceso no autorizado", rol, 500)
    elif rol not in ["admin", "editor"]:
        raise ErrorValidacion("Rol inválido")
    
    print(f"Acceso permitido para el rol {rol}")


roles_a_probar =["visitante", "admin", "superadmin"]

for rol in roles_a_probar:
    print(f"=== PROBANDO ROL {rol} ===")

    try:
        verificar_usuario(rol)
    except ErrorPermisos as e:
        print("Error: no tienes permisos suficientes")
        print(f"Detalle: {e.detalle()}")
        print(f"Código:  {e.codigo}")
        print(f"Rol:  {e.rol}")
    except ErrorValidacion:
        print("Error: datos inválidos")
    except ErrorApplicacion:
        print("Otro error general de aplicación")



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