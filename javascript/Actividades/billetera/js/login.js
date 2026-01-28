const form = document.querySelector("form");

const txtEmail = document.getElementById("idMail");
const txtPass = document.getElementById("idPass");
const feedback = document.querySelector(".invalid-feedback");

form.addEventListener("submit", function (e) {
  e.preventDefault();

  // limpiar estado anterior
  txtEmail.classList.remove("is-invalid");
  txtPass.classList.remove("is-invalid");
  feedback.classList.add("invisible");

  // login simulado
  if (txtEmail.value === "polito@gmail.com" && txtPass.value === "12345") {
    window.location.href = "dashboard.html";
  } else {
    txtEmail.classList.add("is-invalid");
    txtPass.classList.add("is-invalid");
    feedback.classList.remove("invisible");
    limpiarInputsLogin();
  }
});

/**
 * Mostrar / ocultar contraseña
 */
function togglePassword(button) {
  const pass = document.getElementById("idPass");
  const icon = button.querySelector("i");

  if (pass.type === "password") {
    pass.type = "text";
    icon.classList.replace("bi-eye", "bi-eye-slash");
  } else {
    pass.type = "password";
    icon.classList.replace("bi-eye-slash", "bi-eye");
  }
}

function limpiarInputsLogin() {
  setTimeout(() => {
    txtEmail.value = "";
    txtPass.value = "";
    feedback.classList.add("invisible");
    txtEmail.classList.remove("is-invalid");
    txtPass.classList.remove("is-invalid");
  }, 2000);
}
