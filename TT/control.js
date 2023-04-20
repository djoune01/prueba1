$(document).ready(function() {
    $('#myForm').submit(function(event) {
      var name = $('#name').val();
      var password = $('#password').val();
      var email = $('#email').val();
  
      if (name.length < 3) {
        alert('El nombre debe tener al menos 3 caracteres');
        event.preventDefault();
      }
  
      if (password.length < 8) {
        alert('La contraseña debe tener al menos 8 caracteres');
        event.preventDefault();
      }
  
      if (!isValidEmail(email)) {
        alert('El correo electrónico no es válido');
        event.preventDefault();
      }
    });
  
    function isValidEmail(email) {
      var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return emailRegex.test(email);
    }
  });
  