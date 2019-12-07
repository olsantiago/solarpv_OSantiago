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
var UsernameInput = document.getElementById('upusername');
var ClientInput = document.getElementById('client_select');
var FnameInput = document.getElementById('fname');
var MnameInput = document.getElementById('mname');
var LnameInput = document.getElementById('lname');
var EmailInput = document.getElementById('email');
var OphoneInput = document.getElementById('ophone');
var CphoneInput = document.getElementById('cphone');
var JobTitle = document.getElementById('job');
var Prefix = document.getElementById('prefix');

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
button2.addEventListener("submit", function(event){
  event.preventDefault();
  var PostBody = {
    "username": UsernameInput.value,
    "fname": FnameInput.value,
    "lname": LnameInput.value,
    "mname": MnameInput.value,
    "job_title": JobTitle.value,
    "email": EmailInput.value,
    "ophone": OphoneInput.value,
    "cphone": CphoneInput.value,
    "prefix": Prefix.value,
    "client_ID": ClientInput.value
    };
  console.log(PostBody);
  $.post("/backend/api/user/",
  PostBody,
  function(data, status){
    alert("Data: " + data + "\nStatus: " + status);
  });
});
var closeForm2 = function () {
    console.log("Test");
};
document.addEventListener("keyup", function (e) {
    if (e.keyCode == 27 || e.keyCode == 13) {
        closeForm2();
    }
});