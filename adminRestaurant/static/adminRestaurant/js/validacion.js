// Lista de usuarios y contraseñas predefinidas
const users = [
    { usuario: 'usuario1', password: 'contraseña1' },
    { usuario: 'usuario2', password: 'contraseña2' },
    { usuario: 'usuario3', password: 'contraseña3' }
];

// Validación de formulario usando Bootstrap
(function () {
    'use strict';
    window.addEventListener('load', function () {
        // Capturamos todos los formularios con la clase needs-validation
        var forms = document.getElementsByClassName('needs-validation');
        // Iteramos sobre ellos y evitamos el envío si no son válidos
        var validation = Array.prototype.filter.call(forms, function (form) {
            form.addEventListener('submit', function (event) {
                if (form.checkValidity() === false) {
                    event.preventDefault();
                    event.stopPropagation();
                }
                form.classList.add('was-validated');
            }, false);
        });
    }, false);
})();

// Capturamos el formulario de inicio de sesión
const loginForm = document.getElementById('loginForm');
loginForm.addEventListener('submit', function(event) {
    event.preventDefault();
    if (loginForm.checkValidity()) {
        const usuario = document.getElementById('usuario').value;
        const password = document.getElementById('password').value;

        const userExists = users.some(user => user.usuario === usuario && user.password === password);
        
        if (userExists) {
            window.location.href = 'index.html';
        } else {
            alert('Cuenta no encontrada. Por favor, registre una nueva cuenta.');
        }
    }
});

// Capturamos el formulario de registro
const registerForm = document.getElementById('registerForm');
registerForm.addEventListener('submit', function(event) {
    event.preventDefault();
    if (registerForm.checkValidity()) {
        const registerUsuario = document.getElementById('registerUsuario').value;
        const registerEmail = document.getElementById('registerEmail').value;
        const registerPassword = document.getElementById('registerPassword').value;
        const confirmPassword = document.getElementById('confirmPassword').value;

        if (registerPassword !== confirmPassword) {
            alert('Las contraseñas no coinciden.');
            return;
        }

        // Agregar el nuevo usuario a la lista de usuarios
        users.push({ usuario: registerUsuario, password: registerPassword });

        alert('Cuenta creada exitosamente!');
        
        // Cerrar el modal
        var registroModal = bootstrap.Modal.getInstance(document.getElementById('registroModal'));
        registroModal.hide();
    }
});
