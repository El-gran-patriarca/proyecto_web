

$(document).ready(function() {

    $('#imagenPerro').click(function() {
        contadorClicks += 1;
        console.log(contadorClicks);
    })

    $('#joinusName').focusout(function() {
        console.log("Sali del foco")

        if ($('#joinusName')[0].value == '' || $('#joinusName')[0].value == null) {
            document.getElementsByName("joinusNameAlert")[0].classList.remove('hide');
        } else {
            document.getElementsByName("joinusNameAlert")[0].classList.add('hide');
        }
    })
    
    $('#joinus').submit(function(event) {
        console.log("Formulario enviado")
        event.preventDefault();
    });
    
});    