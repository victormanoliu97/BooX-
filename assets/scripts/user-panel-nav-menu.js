var navOpen = false;
var filterOpen = false;
var bookEntryLayout;
var sidePanelHTML;
var filterContainerHTML;

function openNav(steps) {
    if (steps>=0)
    {
        document.body.style.setProperty("grid-template-columns",((15-steps)/4).toString()+"em auto");
        setTimeout(function(){openNav(steps-1)},1000/60);
    }
}
function openFilters(steps) {
    if (steps>5)
    {
        document.getElementById("filterContainer").style.setProperty("height",(3+(10-steps)).toString()+"em");
        setTimeout(function(){openFilters(steps-1)},1000/60);
    }
    else if (steps==5)
    {
        document.getElementById("filterContainer").innerHTML = filterContainerHTML;
        document.getElementById("filterContainer").style.opacity = 0;
        setTimeout(function(){openFilters(steps-1)},1000/60);
    }
    else if (steps>=0)
    {
        document.getElementById("filterContainer").style.opacity = 1-(0.2*steps);
        setTimeout(function(){openFilters(steps-1)},1000/60);
    }
}
function closeFilters(steps) {
    if (steps>5)
    {
        document.getElementById("filterContainer").style.opacity = (1-(0.1*(15-steps)));
        setTimeout(function(){closeFilters(steps-1)},1000/60);
    }
    else if (steps==5)
    {
        document.getElementById("filterContainer").innerHTML = "";
        setTimeout(function(){closeFilters(steps-1)},1000/60);
    }
    else if (steps>=0)
    {
        document.getElementById("filterContainer").style.setProperty("height",(1+steps).toString()+"em");
        setTimeout(function(){closeFilters(steps-1)},1000/60);
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
function switchFilters()
{
    if(filterOpen)
    {
        closeFilters(15);
        filterOpen = false;
    }
    else
    {
        openFilters(15);
        filterOpen = true;
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
        document.getElementById("profileImage").style.backgroundImage = profilePicture;
        document.getElementById("sidePanelButton").classList.remove("fa-arrow-circle-right");
        document.getElementById("sidePanelButton").classList.add("fa-arrow-circle-left");
        openNav(15);
        navOpen = true;
    }
}

function createPopup(url) {
    var newWindow = window.open(url, 'bookOffer', 'height=570, width=900');

    if (window.focus) {
        newWindow.focus();
    }
    return false;
}

function updateDistanceFilter()
{
    document.getElementById("distanceLabel").innerText = "Max distance: " + document.getElementById("distance").value
}


function init()
{
    onLoadGoogleAuthApi();
    sidePanelHTML = document.getElementById("sidePanel").innerHTML;
    document.getElementById("sidePanel").innerHTML = "";
    bookEntryLayout = document.getElementById("main").innerHTML;
    document.getElementById("main").innerHTML = "";
    filterContainerHTML = document.getElementById("filterContainer").innerHTML;
    document.getElementById("filterContainer").innerHTML = "";
    post({},'cgi-bin/getBooks.py',populate);
    // for (var i=0;i<30;i++)
    // {
    //     var container = document.createElement("div");
    //     container.style.width = "15em";
    //     container.style.height = "12em";
    //     container.style.margin = "auto";
    //     container.style.padding = "0.5em";
    //     container.innerHTML = bookEntryLayout;
    //     document.getElementById("main").appendChild(container);
    // }
}


function createUserOffersPopup(url) {
    var newWindow = window.open(url, 'bookOffer', 'height=300, width=700');

    if (window.focus) {
        newWindow.focus();
    }
    return false;
}

function myRedirect() {
    window.location.replace("userOffersTemplate.html");
}

function populate(response)
{
    console.log(response);
    response = JSON.parse(response);
    console.log(response.type);
    if (response.type=='success')
    {
        document.getElementById("main").innerHTML = "";
        response.data.forEach(element => {
            var container = document.createElement("div");
            container.style.width = "15em";
            container.style.height = "12em";
            container.style.margin = "auto";
            container.style.padding = "0.5em";
            container.innerHTML = bookEntryLayout;
            container.getElementsByClassName("bookViewTitle").innerText = element.book.title;
            container.getElementsByClassName("bookViewAuthor").innerText = element.book.author;
            document.getElementById("main").appendChild(container);
        });
    }
    else
    {
        document.getElementById("main").innerHTML = "No Offers at the moment. You can be the first one to publish one. Just click on the plus sign";
    }
}