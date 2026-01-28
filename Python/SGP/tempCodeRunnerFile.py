from app.data.datos_productos import PRODUCTOS
from app.views.opciones_menu import OPCIONES_MENU
from app.views.menu import ejecutar_menu

def main():
    ejecutar_menu(PRODUCTOS, OPCIONES_MENU)

if __name__ == "__main__":
    main()
