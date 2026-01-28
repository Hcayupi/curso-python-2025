/**
 * 2) Calcular precio final con descuento

Enunciado:
Crea una función llamada precioFinal(precio, descuento) que reciba:

- precio (número)
- descuento (porcentaje, por ejemplo 20)

Debe retornar el precio final con el descuento aplicado.

Ejemplos:

- precioFinal(1000, 20) → 800

- precioFinal(5000, 10) → 4500

Pista: descuento en pesos = precio * (descuento / 100).
*/
function  calcularDescuento(precio, descuento){
  let precioFinal= precio-(precio*(descuento/100));

  return precioFinal;
}

let precioTotal = calcularDescuento(5000,20);

console.log(precioTotal);

//////////////////////////////
/**Calcular el doble de un número
Enunciado:

Crea una función llamada calcularDoble(numero) que reciba un número y retorne el doble de ese número.
Luego, pide un número al usuario y muestra el resultado en la consola. */

function calcularDoble(numero){
    return numero * 2;
}

let numero = prompt("Ingrese un número para calcular su doble. ")

console.log("El doble de " + numero + " es: " + calcularDoble(Number(numero)));

/*
1) Saber si un número es par

Enunciado:
Crea una función esPar(numero) que retorne true si el número es par y false si es impar.*/


function esPar(numero){

    if((numero%2)==0){
        return true;
    }else{
        return false;
    }
}

let recibeNumero = prompt("Ingrese un número: ");

let numeroPar = esPar(recibeNumero);

if(numeroPar){
    console.log("El número "+ recibeNumero + " es PAR");
}else{
    console.log("El número "+ recibeNumero + " es IMPAR");
}

/*
2) Convertir grados Celsius a Fahrenheit

Enunciado:
Crea una función celsiusAFahrenheit(c) que reciba grados Celsius y retorne su equivalente en Fahrenheit.
Fórmula: F = (C * 9/5) + 32
*/

function celsiusAFahrenheit(celcius){
    return (celcius*(9/5)) + 32;
}

let gradosCelcius= prompt("Ingrese grados celcius: ");

let gradosF = celsiusAFahrenheit(gradosCelcius);

console.log("Grados Fahrenheit: " + gradosF);

/*
3) Devolver el mayor de dos números

Enunciado:
Crea una función mayor(a, b) que retorne el número más grande. Si son iguales, retorna cualquiera (por ejemplo a).*/

function numeroMayor(a, b){

    if(a == b){
        return "Los números son iguales";
    }

    if(a > b){
        return " El número mayor es: " + a;
    }else{
        return " El número mayor es: "+ b;
    }
}

let primerNumero = prompt("Ingresa el primer número: ");

let segundoNumero = prompt("Ingrese el segundo número: ");


console.log(numeroMayor(primerNumero, segundoNumero));

/*
4) Calcular el área de un rectángulo

Enunciado:
Crea una función areaRectangulo(base, altura) que reciba la base y la altura, y retorne el área.
Fórmula: área = base * altura
*/

function areaRectangulo(base, altura){
    return base*altura;
}

let base = prompt("Ingrese la base:");

let altura = prompt("Ingrese la altura: ");

console.log("El area del rectángulo es : " + areaRectangulo(base, altura));

/*
5) Convertir años a días

Enunciado:
Crea una función aniosADias(anios) que reciba una cantidad de años y retorne cuántos días son (considera que 1 año tiene 365 días).*/


function aniosADias(anios){
    return anios * 365;
}

let anios = prompt("Ingrese la cantidad de años: ");

console.log("Los dias equivalentes son: " + aniosADias(anios));
