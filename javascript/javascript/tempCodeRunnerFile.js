let estudiantes = [
    {nombre: "Ana", nota:6.5},
    {nombre: "Pedro", nota:5.4},
    {nombre: "Juan", nota:5.6},
];

function mostrarAprobados(estudiantes){
    for(let estudiante of estudiantes){
        if(estudiante.nota >= 6){
            console.log(estudiante.nombre + " está aprobado con nota " + estudiante.nota);
        }
    }
}

mostrarAprobados(estudiantes);