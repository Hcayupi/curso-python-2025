"""
Contexto:
Queremos modelar un sistema educativo simple donde los objetos trabajen juntos. 
Algunos se relacionan como partes esenciales (composición), 
mientras que otros cooperan sin depender entre sí (colaboración).
Esto refleja cómo se organiza una plataforma real de cursos.
Consigna:
Vas a crear una clase Curso que contenga un
Docente (composición), y una clase Alumno que se
inscriba a varios cursos (colaboración). Cada clase
tendrá su propia estructura y métodos. El objetivo
es mostrar cómo los objetos se integran en una
estructura completa y funcional.


Composición = estar hecho de
Colaboración = usar

Tiempo : 40 Minutos

Paso a paso:
● Definí la clase Docente con nombre y
especialidad
● Creá la clase Curso que incluya un objeto
Docente como atributo
● Incorporá un método mostrar_info() en
Curso que imprima sus datos y los del
docente
● Definí la clase Alumno con nombre, edad
y una lista de cursos
● Implementá el método mostrar_cursos()
para listar los cursos donde está inscripto
● Probá creando varios objetos y
ejecutando sus métodos
"""

class Docente:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad=especialidad
    
    def __str__(self):
        return f"Nombre:  {self.nombre} | Especialidad: {self.especialidad}"
    
class Curso:

    def __init__(self, nombre_curso, docente):
        self.nombre_curso = nombre_curso
        self.docente = docente

    def __str__(self):
        return f"-{self.nombre_curso}"
    
    def mostrar_info(self):
        print(f"Nombre curso: {self.nombre_curso} | Docente: {self.docente.nombre}")
    


class Alumno:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.cursos = []

    def mostrar_cursos (self):
        print(f"Alumno {self.nombre} está inscrito en: ")
        for curso in self.cursos:
            print("\t\t\t",curso) #Tabulación \t

    def inscribir(self, curso):
        self.cursos.append(curso)


"""
CREACIÓN DE DOCENTES
"""
docente_dagoberto = Docente("Dagoberto", "Matemática")
docente_lalo = Docente("Lalo", "Biología")
docente_maria = Docente("María", "Física")

docente_h_alfredo = Docente("Alfredo", "Historia")
docente_h_vanesa = Docente("Vanesa", "Lenguaje")
docente_h_julio = Docente("Julio", "Filosofía")

print("="*10, "Lista de docentes", "="*10)
print("")
print(docente_dagoberto)
print(docente_lalo)
print(docente_maria)

print(docente_h_alfredo)
print(docente_h_vanesa)
print(docente_h_julio)

"""
CREACIÓN DE CURSOS
"""
print("")
print("="*10, "Lista de cursos", "="*10)
print("")
curso_mat = Curso("Matemática", docente_dagoberto)
curso_bio = Curso("Biología", docente_lalo)
curso_fis = Curso("Física", docente_maria)

curso_h_len = Curso("Lenguaje", docente_h_alfredo)
curso_h_hist = Curso("Historia", docente_h_vanesa)
curso_h_fil = Curso("Filosofía", docente_h_julio)

print(curso_mat)
print(curso_bio)
print(curso_fis)

print(curso_h_len)
print(curso_h_hist)
print(curso_h_fil)

"""
CREACIÓN DE ALUMNOS
"""
alumno_juan = Alumno("Juanito", 12)

alumno_juan.inscribir(curso_mat)
alumno_juan.inscribir(curso_fis)
alumno_juan.inscribir(curso_h_hist)
alumno_juan.inscribir(curso_bio)


alumno_juanita = Alumno("Juanita", 16)
alumno_juanita.inscribir(curso_mat)
alumno_juanita.inscribir(curso_h_len)
alumno_juanita.inscribir(curso_h_hist)


alumno_martina = Alumno("Martina", 15)
alumno_martina.inscribir(curso_h_fil)
alumno_martina.inscribir(curso_h_len)
alumno_martina.inscribir(curso_h_hist)

print("")
print("="*10, "Inscripción de alumnos", "="*10)
print("")
alumno_juan.mostrar_cursos()
alumno_juanita.mostrar_cursos()
alumno_martina.mostrar_cursos()
