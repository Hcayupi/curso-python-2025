
'''
5) Diccionario de alumnos: buscar mejor/peor nota

Enunciado:
Tienes este diccionario de alumnos y sus notas.
Debes mostrar:

El alumno con mejor nota
El alumno con peor nota
El promedio del curso
'''

diccionario_notas={
    "Ana": [6.5, 5.8, 6.2],
    "Luis": [4.9, 5.1, 5.5],
    "Pedro": [6.0, 6.7, 6.4],
    "Sofía": [5.5, 5.9, 6.1]
}

diccionario_ranking={}

def listar_notas():
    for alumnos, notas in diccionario_notas.items():
        print(f" { alumnos } - {notas}")

def ranquear_notas(): 
    nota_mayor = 0.0 
    nota_menor = None
    for alumno, notas in diccionario_notas.items():
        nota_mayor = notas[0.0]

        for nota in notas:
            if notas>nota_mayor:
                nota_mayor = notas  
            
            if notas > nota_mayor:
                nota_menor=notas
                
    diccionario_ranking[alumno]=nota_mayor 
    
    print(f"\n- Peor nota : {nota_menor}")

def analiza_ranking():
    nota_mayor = 0.0 
    nota_menor = 0.0
    alumno_mayor = ""
    alumno_menor = ""
    for clave, nota in diccionario_ranking.items():
        if nota>nota_mayor:
            nota_mayor = nota
            alumno_mayor = clave
        else:
            nota_menor=nota
            alumno_menor=clave            

    print(f" - Mejor nota=  {alumno_mayor} : {nota_mayor}")
listar_notas()
ranquear_notas()
analiza_ranking()


