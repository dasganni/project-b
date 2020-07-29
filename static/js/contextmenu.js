/* $('.btn-container').on("contextmenu", ".btn", function (e) {
    $('.dropdown-menu').css({
        top: e.pageY,
        left: e.pageX,
        display: "block",
    });

    return false;
}); */

$('.contextmenu-container').on("contextmenu", ".contextmenu-item", function (e) {
    $('.dropdown-menu').css({
        top: e.pageY,
        left: e.pageX,
        display: "block",
    });

    return false;
});

/* $('.icon-container').on("contextmenu", ".icon", function (e) {
    $('.dropdown-menu').css({
        top: e.pageY,
        left: e.pageX,
        display: "block",
    });

    return false;
});

$('.card').on("contextmenu", ".card-body", function (e) {
    $('.dropdown-menu').css({
        top: e.pageY,
        left: e.pageX,
        display: "block",
    });

    return false;
});

$('.form-group').on("contextmenu", "input", function (e) {
    $('.dropdown-menu').css({
        top: e.pageY,
        left: e.pageX,
        display: "block",
    });

    return false;
}); */

$(document).click(function (e) {
    // If left click
    if (e.which == 1) {
        $('.dropdown-menu').hide();
    }
    // If right click
    if (e.which == 3) {
        $('.dropdown-menu').hide();
    }
});

$(document).keydown(function (e) {
    // If escape btn
    if (e.which == 27) {
        $('.dropdown-menu').hide();
    }
});