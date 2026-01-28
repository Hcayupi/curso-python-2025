import tkinter as tk

# 1. Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ventana de Color")
ventana.geometry("400x300") # Tamaño inicial de la ventana

# 2. Configurar el color de fondo
# Puedes usar nombres de colores (ej. 'blue', 'lightgray')
# o códigos hexadecimales (ej. '#3498DB')
ventana.configure(bg='blue') # Fondo gris claro

# 3. Añadir elementos (opcional)
# Etiqueta de texto con color
etiqueta = tk.Label(ventana, text="¡Hola, mundo con color!", fg="navy", bg="lightgray", font=("Arial", 16))
etiqueta.pack(pady=20) # Empaqueta la etiqueta en la ventana

# 4. Iniciar el bucle principal para mostrar la ventana
ventana.mainloop()

from pynput import mouse

def al_hacer_click(x, y, boton, presionado):
    if presionado:
        print(f"Click detectado en la posición: ({x}, {y}) con {boton}")

# Inicia el "escuchador" (listener)
with mouse.Listener(on_click=al_hacer_click) as listener:
    listener.join()