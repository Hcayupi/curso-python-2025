Algoritmo Total_compras
	Definir  cantidadCompra, contadorPrecioAlto Como Entero;
	Definir precio, sumaPrecio Como Real;
	
	Escribir "¿Qué cantidad de compras desea realizar?";
	Leer cantidadCompra;
	
	Para i=1 Hasta  cantidadCompra
		
		Escribir "Ingrese precio: ", i;
		Leer precio;
		
		sumaPrecio = sumaPrecio+precio;
		
		SI precio>10000 Entonces
			contadorPrecioAlto = contadorPrecioAlto+1;
		FinSi
	FinPara
	
	Imprimir "Total de compra: $", sumaPrecio;
	Imprimir "Cantidad de compras mayores a $10.000: ", contadorPrecioAlto;
	
FinAlgoritmo
