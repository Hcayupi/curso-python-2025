Algoritmo Asistencia_clases
	
	Definir cantidadEstudiante, contadorAsistencia Como Entero;
	Definir respuesta Como Caracter;
	
	Escribir "¿Cuántos estudiantes hay?";
	Leer cantidadEstudiante;
	
	Para i=1 Hasta cantidadEstudiante
		Escribir "Estudiante ", i , " ¿Asistió a clases? s/n";
		Leer respuesta;
		
		Si respuesta=="s" Entonces
			contadorAsistencia = contadorAsistencia + 1;
		FinSi
	FinPara
	
	Imprimir "Cantidad de estudiantes asistentes: ", contadorAsistencia;
	Imprimir "Cantidad de estudiantes ausentes: ", cantidadEstudiante - contadorAsistencia;
	
FinAlgoritmo
