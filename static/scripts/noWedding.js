var username;

window.onload = function() {
    username = localStorage.getItem('username');
    if (!username) {
        window.location.replace("http://localhost:5000/login");
    }
    
    document.getElementById('createWedButton').onclick = function(){
        window.location.replace(`http://localhost:5000/createWedding?username=${username}`);
    }
    

}
