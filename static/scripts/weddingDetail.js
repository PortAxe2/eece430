var username;
var weddingID;

window.onload = function() {
    var currentUrl = new URL(window.location);
    username = currentUrl.searchParams.get('username');
    weddingID = currentUrl.searchParams.get('weddingID');
    document.getElementById('sendCongrats').setAttribute('action', `/sendCongrats?username=${username}&weddingID=${weddingID}`);
    document.getElementById('sendMoney').setAttribute('action', `/sendMoney?username=${username}&weddingID=${weddingID}`);
    var negativeAmount = Boolean(currentUrl.searchParams.get('negativeAmount'));
    if (negativeAmount) {
        alert("You can't send a negative amount.")
    }
}