var x;
var y;
var z;
var infoWrong;
var signinButton;
var signupButton;
var usernameUsed;

window.onload = function() {

    if(localStorage.getItem('email')) {
        window.location.replace("http://localhost:5000/mainpage");
    }

    x = document.getElementById("login");
    y = document.getElementById("signup");
    z = document.getElementById("btn");

    if (infoWrong == true) {
        document.getElementById('error').style.display = "block";
        setTimeout(function() {
            document.getElementById('error').style.display = "none";
        }, 3000)
    }
    
    signinButton = document.getElementById('signinButton');
    signupButton = document.getElementById('signupButton');

    signinButton.onclick = signinFunction;
    signupButton.onclick = signupFunction;
}

function signup(){
    x.style.left = "-400px";
    y.style.left = "50px";
    z.style.left = "110px";
}
function login(){
    x.style.left = "50px";
    y.style.left = "450px";
    z.style.left = "0px";
}

function signinFunction() {
    usernameUsed = document.getElementById('username2').value;
    console.log(usernameUsed);
    localStorage.setItem('username', usernameUsed);
}

function signupFunction() {
    usernameUsed = document.getElementById('username').value;
    localStorage.setItem('username', usernameUsed);
}

