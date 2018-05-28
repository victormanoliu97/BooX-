function doneOffer() {
    $("#done-button").css('color', 'white');
    $("#done-button").css('background-color', 'green');
}

function removeOffer() {

    if(document.getElementById("done-button").style.backgroundColor == 'green') {
        console.log(document.getElementById("done-button").style.backgroundColor);
        document.getElementById("bookViewInfo").style.display = 'none';
    }
}