var regexExp = /([['"\]])/g;
var regexFilter = /(^[\(][a-zA-Z]{1,}[\s][a-zA-Z]{1,}[,][\s][a-zA-Z]{1,}[^]{1,}[\)]$)/g;
var username;
var deleteButton;
var totalAmount = 0;
var congratsLetters = [];
var moneyContributionsToDelete = [];


window.onload = function() {
    //Get username
    var currentUrl = new URL(window.location);
    username = currentUrl.searchParams.get('username');
    if(username == "admin"){
        document.getElementById('backButton').style.display = "";
    }
    document.getElementById('updateWed').setAttribute('action', `/updateWedding?username=${username}&weddingID=${weddingID}`);
    document.getElementById('backButton').onclick = function goBack() {
        window.history.back();
    };
    console.log(congratsMessages);
    //Set money and congrats messages
    for (i = 0 ; i < congratsMessages.length; i++) {
        var newRow = document.createElement('tr');
        var newData1 = document.createElement('td');
        var newData2 = document.createElement('td');
        newData1.innerHTML = congratsMessages[i].name;
        newData2.innerHTML = congratsMessages[i].message;
        newRow.id = congratsMessages[i].mesID;
        newRow.appendChild(newData1);
        newRow.appendChild(newData2);
        document.getElementById('congratsTable').append(newRow);
    }
    
    for (i = 0 ; i < moneyContributions.length; i++) {
        var newRow = document.createElement('tr');
        var newData1 = document.createElement('td');
        var newData2 = document.createElement('td');
        newData1.innerHTML = moneyContributions[i].name;
        newData2.innerHTML = "$" + moneyContributions[i].amount;
        newRow.id = moneyContributions[i].txID;
        totalAmount += moneyContributions[i].amount;
        newRow.appendChild(newData1);
        newRow.appendChild(newData2);
        document.getElementById('moneyTable').append(newRow);
    }

    //Set total money
    document.getElementById('totalMoney').innerHTML = "$" + totalAmount;

    
    //Set current set date
    var dateee = new Date(document.getElementById('weddingDateValue').innerHTML);
    document.getElementsByName('date')[0].value = dateee.toISOString().slice(0,16);
    
    //Properly list attendees for editing
    var attendees = document.getElementById('attendeesValue').innerHTML;
    var newAttendees = attendees.replaceAll(regexExp, "");
    var attendeesList = newAttendees.split(", ");
    for (i = 0 ; i < attendeesList.length ; i++) {
        addGuest();
        document.getElementsByName('guest[]')[i].value = attendeesList[i];
    }

    //Set delete button
    deleteButton = document.getElementById('deleteWedding');
    document.getElementById('deleteWeddingForm').setAttribute('action', `/deleteWedding?username=${username}&weddingID=${weddingID}`);

    
    window.history.replaceState(null, null, `http://localhost:5000/myWedding?username=${username}&weddingID=${weddingID}`);

}

function cancelEdit() {
    document.getElementById('staticWedding').style.display = "";
    document.getElementById('editWedding').style.display = "none";
}

function startEdit() {
    document.getElementById('staticWedding').style.display = "none";
    document.getElementById('editWedding').style.display = "";
}

function addGuest() {
    var guestsLi = document.getElementsByName('guest[]');
    for (i = 0 ; i < guestsLi.length; i++) {
        if (guestsLi[i].value == "") {
            return;
        }
    }
    // Create a space above each new input
    var br = document.createElement("br");
    // Add input element for each guest
    var row = document.createElement("input");
    //Create div for guest
    var guest = document.createElement("div");
    guest.className = "guestRow";
    row.setAttribute("name", "guest[]");
    row.setAttribute("placeholder", "Enter email or username");
    var buttonDel = document.createElement("input");
    buttonDel.type = "button";
    buttonDel.onclick = deleteGuest;
    buttonDel.value = "-";
    // Add them to the container in the interface
    guest.appendChild(row);
    guest.appendChild(buttonDel);
    document.getElementById("guests").appendChild(guest);
  }

  function deleteGuest(event) {
      var rowDiv = event.target.parentNode;
      rowDiv.remove();
  }