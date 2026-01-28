const links = document.querySelectorAll(".sidebar .nav-link");
const content = document.getElementById("content");

// cargar sección inicial
loadSection("dashboard");

links.forEach((link) => {
  link.addEventListener("click", (e) => {
    e.preventDefault();

    links.forEach((l) => l.classList.remove("active"));
    link.classList.add("active");

    const section = link.dataset.section;
    loadSection(section);
  });
});

function loadSection(section) {
  fetch(`sections/${section}.html`)
    .then((res) => res.text())
    .then((html) => {
      content.innerHTML = html;

      if (section === "dashboard") {
        initDashboardChart();
      }

      if (section === "fondos") {
        initDepositaFondos();
        initRetiroFondos();
      }
      if (section === "envios") {
        initCuentasDestino();
        initNuevaCuenta();
        initEnviarFondos();
        actualizarTablaEnvios();
      }
      if (section === "historial") {
        initHistorialTransaccionas();
      }
    })
    .catch(() => {
      content.innerHTML = "<p>Error al cargar la sección</p>";
    });
}

const toggleBtn = document.getElementById("toggleSidebar");
const sidebar = document.querySelector(".sidebar");
const overlay = document.getElementById("overlay");
const body = document.body;
let chartInstance = null;

toggleBtn.addEventListener("click", () => {
  if (window.innerWidth <= 768) {
    // MOBILE
    sidebar.classList.toggle("show");
    overlay.classList.toggle("show");
    body.classList.toggle("menu-open");
  } else {
    // DESKTOP
    sidebar.classList.toggle("collapsed");
    setTimeout(() => {
      if (chartInstance) {
        chartInstance.resize();
      }
    }, 300);
  }
});
overlay.addEventListener("click", () => {
  sidebar.classList.remove("show", "collapsed");
  overlay.classList.remove("show");
  body.classList.remove("menu-open");
});

window.addEventListener("resize", () => {
  if (chartInstance) {
    chartInstance.resize();
  }
});

/** Función que evita que se ejecute el grafico
 * chart antes que se cargue el dashboard */

function initDashboardChart() {
  const chartDom = document.getElementById("movimientosChart");
  if (!chartDom) return;

  if (chartInstance) {
    chartInstance.dispose();
  }

  chartInstance = echarts.init(chartDom);

  const option = {
    tooltip: {
      trigger: "axis",
    },
    legend: {
      top: 10,
      left: "center",
    },
    grid: {
      top: 60,
      left: "3%",
      right: "4%",
      bottom: "10%",
      containLabel: true,
    },
    xAxis: {
      type: "category",
      boundaryGap: false,
      data: ["Ene", "Feb", "Mar", "Abr", "May", "Jun"],
    },
    yAxis: {
      type: "value",
    },
    series: [
      {
        name: "Ingresos",
        type: "line",
        smooth: true,
        data: [100000, 500000, 400000, 600000, 800000, 900000],
        lineStyle: {
          width: 3,
        },
      },
      {
        name: "Retiros",
        type: "line",
        smooth: true,
        data: [110000, 120000, 300000, 200000, 400000, 500000],
        lineStyle: {
          width: 3,
        },
      },
    ],
  };

  chartInstance.setOption(option);

  chartInstance.setOption(option);
}
