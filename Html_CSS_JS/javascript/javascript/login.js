const prompt = require('prompt-sync')();

let usuarioValido = "user123";
let contrasenaValida = "pass123";

let usuario = prompt("Ingrese usuario: ");
let contrasena = prompt("Ingrese contraseña: ");

if (usuario === usuarioValido && contrasena === contrasenaValida) {
    console.log(`Login exitoso. ¡Bienvenido ${usuario}!`);
} else {
    console.log("Login fallido. Usuario o contraseña incorrectos.");
}