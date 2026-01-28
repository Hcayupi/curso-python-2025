#Ejemplo función normal
def sumar(a, b):
    return a + b

print(sumar(3, 5))  # 8

#La misma función con lambda:
sumar = lambda a, b: a + b

print(sumar(3, 5))  # 8

#Otros ejemplos
#? Duplicar un número
def duplicar(x):
    return x * 2

duplicar = lambda x: x * 2
print(duplicar(4))  # 8


#? Ver si un número es par
def es_par(n):
    if n % 2 == 0:
        return True
    else:
        return False

es_par = lambda n: n % 2 == 0
print(es_par(6))  # True

hora = 22
mensaje = (lambda h: "Buenas noches" if h >= 20 else "Buen día")(hora)
print(mensaje)

def contar(n):#0
    if n == 0:        # caso base
        print("Fin")
    else:
        print(n)#1
        contar(n - 1)#1-1 = 0 # llamada recursiva


contar(5)

import tkinter as tk
from datetime import datetime, timedelta

def actualizar_reloj():
    ahora = datetime.now()
    fin_clase = ahora.replace(hour=22, minute=30, second=0)

    if ahora > fin_clase:
        restante = timedelta(0)
    else:
        restante = fin_clase - ahora

    horas, resto = divmod(restante.seconds, 3600)
    minutos, segundos = divmod(resto, 60)

    hora_actual = ahora.strftime("%H:%M:%S")

    etiqueta.config(
        text=f"Son las {hora_actual}\n"
            f"Faltan {horas:02d}:{minutos:02d}:{segundos:02d} para que finalice la clase"
    )

    etiqueta.after(1000, actualizar_reloj)

ventana = tk.Tk()
ventana.title("Cuenta regresiva clase")
etiqueta = tk.Label(ventana, font=("Helvetica", 36), fg="blue")
etiqueta.pack(padx=20, pady=20)

actualizar_reloj()
ventana.mainloop()
