
const factorGravedad = 0.38;

let personas = [];

function calcularPesoEnMarte(pesoEnTierra) {
  return pesoEnTierra * factorGravedad;
}

function validaPeso(peso) {
  let pesoNumerico = Number(peso);

  if (Number.isNaN(pesoNumerico)) {
    console.log("\n  -- Solo se permite valores numéricos -- \n");
    return false;
  }
  if (pesoNumerico <= 0) {
    console.log(
      "\n -- El peso ingresado no es válido, debe ser mayor a 0. -- \n"
    );
    return false;
  }
  return true;
}

let nombrePersona, apellidoPersona, pesoEnTierra, pesoEnMarte;
let masIngresos;

do {
  console.clear();
  nombrePersona = prompt("\nIngrese nombre: ");
  apellidoPersona = prompt("Ingrese apellido: ");

  do {
    pesoEnTierra = prompt("Ingrese peso: ");
  } while (!validaPeso(pesoEnTierra));

  let pesoEnMarte = calcularPesoEnMarte(pesoEnTierra);
  
  personas.push({
    nombre: nombrePersona,
    apellido: apellidoPersona,
    peso: pesoEnTierra,
    pesoMarciano: pesoEnMarte.toFixed(2),
  });

  do {
    masIngresos = prompt("\n¿Desea realizar más registro: s/n?:")
      .toLowerCase()
      .trim();
  } while (masIngresos !== "s" && masIngresos !== "n");
} while (masIngresos === "s");

console.clear();
console.log("\n------ LISTA DE PERSONAS REGISTRADAS -------\n");

for (let persona of personas) {
  console.log("\n-Persona : " + persona.nombre + " " + persona.apellido + ".");
  console.log("-Peso en la Tierra: " + persona.peso + " kg.");
  console.log("-Peso en Marte: " + persona.pesoMarciano + " kg.");
  console.log("\n-       -        -        -        -");
}
console.log("\n");
