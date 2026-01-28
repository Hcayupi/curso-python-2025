Algoritmo Juego_puntajes
	Definir cantidadJugadores, puntajeMayor, puntaje, sumaPuntaje Como Entero;
	
	Escribir "¿Cuál es la cantidad de jugadores?";
	Leer cantidadJugadores;
	
	puntajeMayor = 0;
	Para i=1 Hasta cantidadJugadores
		
		Escribir "Puntaje de jugador ", i;
		Leer puntaje;
		
		Si puntaje>puntajeMayor Entonces
			puntajeMayor = puntaje;
		FinSi
		
		sumaPuntaje = sumaPuntaje + puntaje;
		
	FinPara
	
	Escribir "Puntaje total: ", sumaPuntaje;
	Escribir "Puntaje mayor: ", puntajeMayor;
	
FinAlgoritmo
