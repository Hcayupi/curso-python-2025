let movimiento = [
  {
    fecha: "10-06-2025",
    tipo: "Deposito",
    monto: 50000,
    detalle: "Ingreso incial",
  },
  {
    fecha: "12-06-2025",
    tipo: "Retiro",
    monto: 30000,
    detalle: "Transferencia",
  },
];

function initDepositaFondos() {
  const botonMonto = document.getElementById("idButtonMonto");

  console.log("Inicializando transacciones, botón:", botonMonto);

  if (!botonMonto) {
    console.log("Botón NO encontrado (vista no cargada)");
    return;
  }

  botonMonto.addEventListener("click", function () {
    const montoDeposito = document.getElementById("idMontoDeposito");
    const detalleDeposito = document.getElementById("idDetalleDeposito");

    if (montoDeposito.value === "" || detalleDeposito.value === "") {
      alert("Completa todos los campos");
      return;
    }

    movimiento.push({
      fecha: new Date().toLocaleDateString("es-CL"),
      tipo: "Depósito",
      monto: Number(montoDeposito.value),
      detalle: detalleDeposito.value,
    });

    actualizarTablaFondo();

    montoDeposito.value = "";
    detalleDeposito.value = "";
  });

  actualizarTablaFondo();
}


function actualizarTablaFondo() {
  const tbody = document.querySelector("#idTablaHistorial tbody");

  if (!tbody) return;

  tbody.innerHTML = "";

  movimiento.forEach((mov) => {
    let color = mov.tipo === "Depósito" ? "text-success" : "text-danger";
    let signo = mov.tipo === "Depósito" ? "" : "-";

    tbody.innerHTML += `
            <tr>
                <td>${mov.fecha}</td>
                <td>${mov.tipo}</td>
                <td>${mov.detalle}</td>
                <td class="${color}">${signo}$${mov.monto.toLocaleString()}</td>
            </tr>
        `;
  });
}

function initRetiroFondos() {
  const botonMonto = document.getElementById("idRetirarButton");

  console.log("Inicializando transacciones, botón:", botonMonto);

  if (!botonMonto) {
    console.log("Botón NO encontrado (vista no cargada)");
    return;
  }

  botonMonto.addEventListener("click", function () {
    const montoDeposito = document.getElementById("idMontoRetiro");
    const detalleDeposito = document.getElementById("idDescripcionRetiro");

    if (montoDeposito.value === "" || detalleDeposito.value === "") {
      alert("Completa todos los campos");
      return;
    }

    movimiento.push({
      fecha: new Date().toLocaleDateString("es-CL"),
      tipo: "Retiro",
      monto: Number(montoDeposito.value),
      detalle: detalleDeposito.value,
    });

    actualizarTablaFondo();

    montoDeposito.value = "";
    detalleDeposito.value = "";
  });

  actualizarTablaFondo();
}