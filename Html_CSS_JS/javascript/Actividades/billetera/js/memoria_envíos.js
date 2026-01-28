const cuentas = [
  { id: "123-456", nombre: "Cuenta 123-456" },
  { id: "987-654", nombre: "Cuenta 987-654" },
  { id: "111-222", nombre: "Cuenta 111-222" },
];

let historialEnvios = [];

function initNuevaCuenta() {
  const nombreCuenta = document.getElementById("idNombreCuenta");
  const numeroCuenta = document.getElementById("idNumeroCuenta");
  const botonNuevaCuenta = document.getElementById("idButtonCuentaNueva");

  if (!nombreCuenta || !numeroCuenta || !botonNuevaCuenta) return;

  botonNuevaCuenta.addEventListener("click", function () {
    const nombre = nombreCuenta.value.trim();
    const numero = numeroCuenta.value.trim();

    if (nombre === "" || numero === "") {
      alert("Debe ingresar nombre y número de cuenta");
      return;
    }

    cuentas.push({
      id: numero,
      nombre: `${nombre} ${numero}`,
    });

    nombreCuenta.value = "";
    numeroCuenta.value = "";

    initCuentasDestino();

    const modalElement = document.getElementById("modalNuevaCuenta");
    const modal = bootstrap.Modal.getOrCreateInstance(modalElement);
    modal.hide();
  });
}

function initCuentasDestino() {
  const select = document.getElementById("idCuentaDestino");
  if (!select) return;

  select.innerHTML = `<option value="">Seleccione cuenta</option>`;

  cuentas.forEach((cuenta) => {
    const option = document.createElement("option");
    option.value = cuenta.id;
    option.textContent = cuenta.nombre;
    select.appendChild(option);
  });
}

function initEnviarFondos() {
  const btnEnviar = document.getElementById("idEnviarFondos");
  const cuentaSelect = document.getElementById("idCuentaDestino");
  const detalleInput = document.getElementById("idDetalleEnvio");
  const montoInput = document.getElementById("idMontoEnvio");

  if (!btnEnviar || !cuentaSelect || !detalleInput || !montoInput) {
    console.warn("Elementos de envío no encontrados");
    return;
  }

  btnEnviar.addEventListener("click", function () {
    const cuenta = cuentaSelect.value;
    const detalle = detalleInput.value.trim();
    const monto = Number(montoInput.value);

    if (cuenta === "" || detalle === "" || monto <= 0) {
      alert("Complete todos los campos correctamente");
      return;
    }

    historialEnvios.push({
      fecha: new Date().toLocaleDateString("es-CL"),
      cuenta,
      detalle,
      monto,
    });

    detalleInput.value = "";
    montoInput.value = "";
    cuentaSelect.innerHTML = `<option value="">Seleccione cuenta</option>`;

    actualizarTablaEnvios();
  });
}

function actualizarTablaEnvios() {
  const tbody = document.querySelector("#idTablaHistorialEnvios tbody");
  if (!tbody) return;

  tbody.innerHTML = "";

  historialEnvios.forEach((mov) => {
    tbody.innerHTML += `
      <tr>
        <td>${mov.fecha}</td>
        <td>${mov.cuenta}</td>
        <td>${mov.detalle}</td>
        <td class="text-success">$${mov.monto.toLocaleString()}</td>
      </tr>
    `;
  });
}
