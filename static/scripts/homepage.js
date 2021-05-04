var navChoices;
var username;
var events;
var weddingsJSON;

window.onload = function() {
    username = localStorage.getItem('username');
    console.log(username);
    if (!username) {
        window.location.replace("http://localhost:5000/login");
    }
    events = document.getElementById('eventss');
    
    weddingsJSON = JSON.parse(weddings);
    console.log(weddingsJSON);
    for (i = 0 ; i < weddingsJSON.length ; i++) {
        var anchorLink = document.createElement('a');
        anchorLink.href = `http://localhost:5000/weddingDetail?username=${username}&weddingID=${weddingsJSON[i].weddingID}`;
        var newWed = document.createElement('div');
        newWed.className = "event";
        var backgroundIm = `linear-gradient(to bottom, rgba(245, 246, 252, 0.2), rgba(117, 19, 93, 0.5)), url(${weddingsJSON[i].imageURL})`;
        newWed.style.backgroundImage = backgroundIm;
        var coupleNames = document.createElement('p');
        coupleNames.innerHTML = `${weddingsJSON[i].brideName} and ${weddingsJSON[i].groomName}`;
        newWed.appendChild(coupleNames);
        anchorLink.appendChild(newWed);
        events.appendChild(anchorLink);
    }
}

function pageChanged(choice) {
    for (i = 0 ; i < navChoices.length ; i++) {
        navChoices[i].className = "";
    }
    choice.className = "active";
}