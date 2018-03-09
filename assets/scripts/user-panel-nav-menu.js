function openNav() {
    document.getElementById("mySidenav").style.width = "150px";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}

function createPopup(url) {
    var newWindow = window.open(url, 'bookOffer', 'height=620, width=900');

    if (window.focus) {
        newWindow.focus();
    }
    return false;
}