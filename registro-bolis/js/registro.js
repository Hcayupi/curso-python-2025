 // ----------------------------------------------------
        // CONFIG: Pega aquí la URL de tu Web App (Google Apps Script)
        // ----------------------------------------------------
        const apiBaseUrl = "https://script.google.com/macros/s/AKfycbyMBgXtVVvOYNS0c0f1k28YvZvt0-q94eRMYGRMter8i5iIE1dV1aXdjFzJBCZpM3OKvQ/exec"; // <- reemplaza esto

        // Recomendación: sirve este index.html desde un servidor local (ej: python -m http.server)

        // Modal bootstrap
        const modalEl = document.getElementById('modalForm');
        const bsModal = new bootstrap.Modal(modalEl);

        const tblBody = document.querySelector('#tblRegistros tbody');
        const form = document.getElementById('formRegistro');

        document.getElementById('btnNew').addEventListener('click', () => openForm());
        document.getElementById('btnRefresh').addEventListener('click', loadAll);

        document.addEventListener("DOMContentLoaded", () => {
            const cantidad = document.getElementById("inputCantidad");
            const precio = document.getElementById("inputPrecio");
            const total = document.getElementById("inputTotal");

            function calcularTotal() {
                const c = parseFloat(cantidad.value) || 0;
                const p = parseFloat(precio.value) || 0;
                total.value = (c * p).toFixed(0);
            }

            cantidad.addEventListener("input", calcularTotal);
            precio.addEventListener("input", calcularTotal);
        });

        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            const id = document.getElementById('registroId').value;


            const payload = {
                id,
                nombre: document.getElementById('inputNombre').value,
                modalidad: document.getElementById('inputModalidad').value,
                producto: document.getElementById('inputProducto').value,
                envase: document.getElementById('inputEnvase').value,
                cantidad: document.getElementById('inputCantidad').value,
                precio: document.getElementById('inputPrecio').value,
                total: document.getElementById('inputTotal').value,
                fecha: document.getElementById('inputFecha').value
            };

            try {
                if (!apiBaseUrl || apiBaseUrl.includes('TU_URL')) throw new Error('Pega la URL de tu Apps Script en apiBaseUrl.');
                const action = id ? 'update' : 'create';
                const res = await fetch(apiBaseUrl, {
                    method: 'POST',
                    body: JSON.stringify({ action, data: payload })
                });

                const json = await res.json();
                if (json.ok) {
                    bsModal.hide();
                    loadAll();
                } else alert('Error: ' + (json.error || 'respuesta no OK'));
            } catch (err) {
                alert('Error: ' + err.message);
            }
        });

        // Cargar todos los registros
        async function loadAll() {
            try {
                if (!apiBaseUrl || apiBaseUrl.includes('TU_URL')) throw new Error('Pega la URL de tu Apps Script en apiBaseUrl.');
                const res = await fetch(apiBaseUrl + '?action=list');
                const json = await res.json();
                if (!json.ok) throw new Error(json.error || 'No OK');

                renderTable(json.data || []);
            } catch (err) {
                alert('No fue posible cargar los registros: ' + err.message + '\n\nRecomendación: sirve este archivo con un servidor local y asegúrate de que la Web App esté desplegada como "Cualquiera con el enlace".');
            }
        }

        function renderTable(rows) {
            tblBody.innerHTML = '';
            rows.forEach((r, i) => {
                const tr = document.createElement('tr');
                const fechaLocal = new Date(r.fecha).toISOString().substring(0, 10);
                tr.innerHTML = `
        <td>${i + 1}</td>
        <td>${escapeHtml(r.nombre)}</td>
        <td>${escapeHtml(r.modalidad)}</td>
        <td>${escapeHtml(r.producto)}</td>
        <td>${escapeHtml(r.envase)}</td>
        <td>${escapeHtml(r.cantidad)}</td>
        <td>${escapeHtml(r.precio)}</td>
        <td>${escapeHtml(r.total)}</td>
        
        <td>${escapeHtml(fechaLocal)}</td>
        <td>
          <button class="btn btn-sm btn-outline-primary btn-edit" data-id="${r.id}">Editar</button>
          <button class="btn btn-sm btn-outline-danger btn-del" data-id="${r.id}">Eliminar</button>
        </td>
      `;
                tblBody.appendChild(tr);
            });

            // attach handlers
            document.querySelectorAll('.btn-edit').forEach(btn => {
                btn.addEventListener('click', async () => {
                    const id = btn.getAttribute('data-id');
                    const row = rows.find(x => x.id === id);
                    if (row) openForm(row);
                });
            });

            document.querySelectorAll('.btn-del').forEach(btn => {
                btn.addEventListener('click', async () => {
                    const id = btn.getAttribute('data-id');
                    if (!confirm('Eliminar registro?')) return;
                    try {
                        const res = await fetch(apiBaseUrl, {
                            method: 'POST',
                            body: JSON.stringify({ action: 'delete', data: { id } })
                        });
                        const json = await res.json();
                        if (json.ok) loadAll(); else alert('Error: ' + (json.error || 'no OK'));
                    } catch (err) {
                        alert('Error: ' + err.message);
                    }
                });
            });
        }

        function openForm(row = null) {
            document.getElementById('registroId').value = row ? row.id : '';
            document.getElementById('inputNombre').value = row ? row.nombre : '';
            document.getElementById('inputModalidad').value = row ? row.modalidad : '';
            document.getElementById('inputProducto').value = row ? row.producto : '';
            document.getElementById('inputEnvase').value = row ? row.envase : '';
            document.getElementById('inputCantidad').value = row ? row.cantidad : '';
            document.getElementById('inputPrecio').value = row ? row.precio : '';
            document.getElementById('inputTotal').value = row ? row.total : '';
            document.getElementById('inputFecha').value = row ? row.fecha : '';


            document.getElementById('modalTitle').textContent = row ? 'Editar registro' : 'Nuevo registro';
            bsModal.show();
        }

        // Escapa texto simple para evitar HTML injection
        function escapeHtml(s) {
            if (s == null) return '';
            return String(s).replace(/[&<>"']/g, (c) => ({
                '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
            })[c]);
        }

        // carga inicial
        loadAll();