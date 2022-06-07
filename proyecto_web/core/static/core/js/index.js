$(document).ready(function() {
    $('.js-tilt').tilt({
        scale: 1.2
    })
    var options = {
        width: 450, // required
        scale: 0.7
    };

    //new ImageZoom(document.getElementById("prod-principal"), options);
    $("#prod-principal").elevateZoom({scrollZoom : true});
});  