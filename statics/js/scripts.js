var button = document.querySelector("#signIn");
var openForm = function () {
    button.className = 'active';
};
var checkInput = function (input) {
    if (input.value.length > 0) {
        input.className = 'active';
    } else {
        input.className = '';
    }
};
var closeForm = function () {
    button.className = '';
};
document.addEventListener("keyup", function (e) {
    if (e.keyCode == 27 || e.keyCode == 13) {
        closeForm();
    }
});


var button2 = document.querySelector("#signUp");
var openForm2 = function () {
    button2.className = 'active';
};
var checkInput = function (input) {
    if (input.value.length > 0) {
        input.className = 'active';
    } else {
        input.className = '';
    }
};
var closeForm2 = function () {
    button2.className = '';
};
document.addEventListener("keyup", function (e) {
    if (e.keyCode == 27 || e.keyCode == 13) {
        closeForm2();
    }
});