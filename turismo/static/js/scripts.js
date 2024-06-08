$(document).ready(function(){
    $("#fomurlario-sing-in").submit(function(event){ 
    event.preventDefault();

    var nombre = $("#name-sing-in").val();
    var password = $("#password-sing-in").val();

    if(nombre.length < 3 || nombre.length > 20){
        alert("El Nombre debe tener entre 3 y 20 caracteres.");
        return;
    }
    if(password.length < 3 || password.length > 20){
        alert("La contraseña debe tener entre 3 y 20 caracteres.");
        return;
    }
    alert("¡Registro exitoso!");
    });
});
