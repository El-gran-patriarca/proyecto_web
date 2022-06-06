$(document).ready(function () {
    
    $("input.form-control").on("keypress",
        function (e) {
            if (e.which == 13) {
                e.preventDefault();
                var $next = $('[tabIndex=' + (+this.tabIndex + 1) + ']');
                //console.log($next.length);
                if (!$next.length) {
                    //$next = $('[tabIndex=1]');      
                    $next = $('#bnt-aceptar');
                }
                $next.focus();
            }
            // TODO: For last TextField, do nothing
        });

    $('#joinusEmail').focusout(function () {
        console.log("Sali del foco")

        if ($('#joinusEmail')[0].value == '' || $('#joinusEmail')[0].value == null) {
            document.getElementsByName("joinusEmailAlert")[0].classList.remove('d-none');
        } else {
            document.getElementsByName("joinusEmailAlert")[0].classList.add('d-none');
        }
    })

    $('#joinusPassword').focusout(function () {
        console.log("Sali del foco")

        if ($('#joinusPassword')[0].value == '' || $('#joinusPassword')[0].value == null) {
            document.getElementsByName("joinusPasswordAlert")[0].classList.remove('d-none');
        } else {
            document.getElementsByName("joinusPasswordAlert")[0].classList.add('d-none');
        }
    })

    $('#joinus').submit(function (event) {
        console.log("Formulario enviado")
        event.preventDefault();
    });

});        