function initHistorialTransaccionas() {
  const tbody = document.querySelector("#idTablaHistorialTransacciones tbody");
  if (!tbody) return;

  tbody.innerHTML = "";
  if (historialEnvios.length > 0) {
    historialEnvios.forEach((mov) => {
      tbody.innerHTML += `
      <tr>
        <td>${mov.fecha}</td>
        <td>Envío</td>
        <td>${mov.detalle}</td>
        <td class="text-success">$${mov.monto.toLocaleString()}</td>
      </tr>
    `;
    });
  }

  if (movimiento.length > 0) {
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
}
