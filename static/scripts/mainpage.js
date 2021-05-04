var logout;
var username;

window.onload = function() {
    username = localStorage.getItem('username');
    if (!username) {
        window.location.replace("http://localhost:5000/login");
    }
    
    logout = document.getElementById('logout');
    logout.onclick = logoutFunction;
    document.getElementById('weddingList').onclick = function(){
        window.location.replace(`http://localhost:5000/homepage?username=${username}`);
    }

    document.getElementById('myWedding').onclick = function() {
        window.location.replace(`http://localhost:5000/myWedding?username=${username}`)
    }
 
    document.getElementById('createWedding').onclick = function() {
        window.location.replace(`http://localhost:5000/createWedding?username=${username}`);
    }

    
    document.getElementById('createWedding2').onclick = function() {
        window.location.replace(`http://localhost:5000/createWedding?username=${username}`);
    }
    
    window.history.replaceState(null, null, `http://localhost:5000/mainpage?username=${username}`);
}

function logoutFunction() {
    localStorage.clear("username");
    window.location.replace("http://localhost:5000/login");
}
