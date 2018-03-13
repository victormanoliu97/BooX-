var navOpen = false;
var sidePanelHTML;
function openNav(steps) {
    if (steps>=0)
    {
        document.body.style.setProperty("grid-template-columns",((15-steps)/4).toString()+"em auto");
        setTimeout(function(){openNav(steps-1)},1000/60);
    }
}

function closeNav(steps)
{
    if (steps>=0)
    {
        document.body.style.setProperty("grid-template-columns",(steps/4).toString()+"em auto");
        setTimeout(function(){closeNav(steps-1)},1000/60);
    }
    else
    {
        document.getElementById("sidePanel").innerHTML = "";
    }
}
function switchNav()
{
    if(navOpen)
    {
        document.getElementById("sidePanelButton").classList.remove("fa-arrow-circle-left");
        document.getElementById("sidePanelButton").classList.add("fa-arrow-circle-right");
        closeNav(15);
        navOpen = false;
    }
    else
    {
        document.getElementById("sidePanel").innerHTML = sidePanelHTML;
        document.getElementById("sidePanelButton").classList.remove("fa-arrow-circle-right");
        document.getElementById("sidePanelButton").classList.add("fa-arrow-circle-left");
        openNav(15);
        navOpen = true;
    }
}

function createPopup(url) {
    var newWindow = window.open(url, 'bookOffer', 'height=620, width=900');

    if (window.focus) {
        newWindow.focus();
    }
    return false;
}

function closePopup() {
    window.close();
}

function init()
{
    sidePanelHTML = document.getElementById("sidePanel").innerHTML;
    document.getElementById("sidePanel").innerHTML = "";
}

