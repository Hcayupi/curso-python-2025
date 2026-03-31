"""
POO #1: Clase Reproductor (playlist)

Objetivo: composición + “sobrecarga” por *args + __str__.

Enunciado

Crea estas clases:

1) Cancion
* Atributos: titulo, artista, duracion_seg
* Implementa __str__ para mostrar: "Título - Artista (mm:ss)"

2) Playlist (composición)
* Contiene una lista de canciones (parte esencial)
* Método agregar(cancion)

3) Reproductor (colaboración)
* Tiene un método reproducir(playlist, *args) que funcione así:
    - Sin args → reproduce “toda la playlist” (imprime cada canción)
    - 1 arg (n) → reproduce las primeras n canciones
    - 2 args (inicio, fin) → reproduce desde inicio hasta fin (inclusive)
    - Si args inválidos → error

Condiciones
* Validar rangos (inicio/fin no pueden salir del tamaño de la playlist)
* No usar libr
'''
POO #2: Clase Tarea y Agenda (organizador)

Objetivo: @classmethod, @staticmethod, atributo de clase, “sobrecarga” con defaults + **kwargs.

Enunciado

Crea estas clases:

1) Tarea
* Atributos: titulo, prioridad (1 a 5), hecha (bool)
* Atributo de clase: prioridad_por_defecto = 3
* @staticmethod prioridad_valida(p) → retorna True si está entre 1 y 5
* @classmethod cambiar_prioridad_defecto(nueva) → cambia la prioridad por defecto si es válida
* Implementa __str__ para mostrar:
    - "[ ] Título (prio X)" si no está hecha
    - "[x] Título (prio X)" si está hecha

2) Agenda (composición)
* Contiene una lista de tareas
* Método agregar(titulo, **kwargs) que simule sobrecarga:
    - Si kwargs trae prioridad, úsala (validándola)
    - Si no trae, usar Tarea.prioridad_por_defecto
    - Si trae hecha=True/False, asignarla (si no, False)

* Método marcar_hecha(indice) para marcar una tarea como lista
* Método mostrar() para imprimir todas

Casos de prueba esperados:
* Cambiar prioridad por defecto a 5 y agregar tareas sin prioridad
* Agregar tarea con prioridad inválida (debe rechazar o corregir)
* Mostrar agenda con __str__
"""


class Cancion:

    def __init__(self, titulo, artista, duracion_seg=0):
        self.titulo = titulo
        self.artista = artista
        self.duracion_seg= duracion_seg

    def __str__(self):
        minutos = self.duracion_seg // 60
        segundos = self.duracion_seg % 60
        return f"{self.titulo} - {self.artista} ({self.minutos:02d} : {self.segundos:02d})"
    
class Playlist:
    def __init__(self):
        self.canciones = []
    
    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)
    
    def get_canciones(self):
        return self.canciones

class Reproductor:

    def reproducir(self, playlist, *rango):
        if not Reproductor.valida_opciones(rango):
            print("Rango inválido")

        if len(playlist.get_canciones()) == 0:
            print("No hay canciones en la playlist...")
            return

        if len(rango) == 0:
            print("Reproduciendo toda la playlist")
            return
        
        if len(rango)==1:
            cantidad = rango[0]
            print(f"Reproducir {cantidad} canciones")
            return
        
        if len(rango) ==2:
            inicio = rango[0]
            final = rango[1]
            print(f"Se reproduce desde {inicio} hasta {final}")
            return

    @staticmethod
    def valida_opciones(self, *rango):
        if len(rango)>2:
            return False
        if len(rango)>0:
            if not isinstance(rango[0], int) or not isinstance(rango[1], int):
                return False



cancion_uno = Cancion("Imagine","John Lennon",183)

playlist = Playlist()

playlist.agregar_cancion(cancion_uno)


reproductor = Reproductor()

reproductor.reproducir(playlist,1,2,3)







