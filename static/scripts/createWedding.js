var logout;

window.onload = function() {
    logout = document.getElementById('logout');
    logout.onclick = logoutFunction;
}

function logoutFunction() {
    localStorage.clear("username");
    window.location.replace("http://localhost:5000/login");
}
