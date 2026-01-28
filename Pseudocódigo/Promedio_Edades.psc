Algoritmo Promedio_Edades
	
	Definir contador, cantidadPersonas, edad, sumaEdad, edadMayor Como Entero;
	Definir promedio Como Real;
	
	Escribir "Ingrese cantidad de personas";
	Leer cantidadPersonas;
	
	contador=1;
	edadMayor=0;
	
	Mientras contador<=cantidadPersonas Hacer
		Escribir "Ingrese edad de persona : ", contador;
		Leer edad;
		
		Si edad>edadMayor Entonces
			edadMayor = edad;
		FinSi
		
		sumaEdad = sumaEdad + edad;
		contador=contador+1;
	FinMientras
	
	promedio = sumaEdad/cantidadPersonas;
	
	Imprimir "El promedio de las edades es: ", promedio;
	Imprimir "Edad mayor: ", edadMayor; 
	
FinAlgoritmo
