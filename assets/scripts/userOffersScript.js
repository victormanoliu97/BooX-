
var navOpen = false;
var filterOpen = false;
var bookEntryLayout;
var sidePanelHTML;

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

function init()
{
    json = {};
    json.apikey = currentUserApiKey;
    console.log(currentUserApiKey);
    sidePanelHTML = document.getElementById("sidePanel").innerHTML;
    document.getElementById("sidePanel").innerHTML = "";
    bookEntryLayout = document.getElementById("main").innerHTML;
    document.getElementById("main").innerHTML = "";
    
    console.log('nu')
    get(json, 'cgi-bin/userOffers.py',populate);
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
            container.style.height = "fit-content";
            container.style.margin = "auto";
            container.style.padding = "0.5em";
            container.innerHTML = bookEntryLayout;
            container.getElementsByClassName("bookViewTitle")[0].innerText = element.book.title;
            if(element.done==0)
            {
                container.getElementsByClassName("submitButton")[0].onclick = function(){terminateOffer(element.id)};
                container.getElementsByClassName("submitButton")[0].id = "done_button_"+element.id;
            }
            else
            {
                container.getElementsByClassName("submitButton")[0].remove()
            }
            // addListener(container.getElementsByClassName("button")[0],'click',terminateOffer(element.book.id));
            container.getElementsByClassName("bookViewAuthor")[0].innerText = element.book.author;
            container.getElementsByClassName("bookViewImage")[0].style.backgroundImage = "url("+element.book.thumbnail+")";
            document.getElementById("main").appendChild(container);
        });
    }
    else
    {
        document.getElementById("main").innerHTML = "No Offers at the moment. You can be the first one to publish one. Just click on the plus sign";
    }
}

function terminateOffer(id)
{
    put({'id':id,'apikey':currentUserApiKey},'cgi-bin/done.py',terminateOfferCallback);
}
function terminateOfferCallback(response)
{
    console.log(response)
    response = JSON.parse(response);
    if(response.type=='success')
    {
        console.log("done_button_"+response.id)
        document.getElementById("done_button_"+response.id).remove();
    }
    else if(response.type=='error')
    {
        document.body.innerHTML = '<h1 id="message">'+response.message+"</h1>";
        document.getElementById("message").style.color = 'red';
    }
}
