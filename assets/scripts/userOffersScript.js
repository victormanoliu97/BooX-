var auth2 = null;
function doneOffer() {
    console.log('You clicked me');
    document.getElementById('done-button').style = 'background-color:green';
}


function initialize()
{
    json = {};
    json.email = 'victormanoliu97@gmail.com';
    sidePanelHTML = document.getElementById("sidePanel").innerHTML;
    document.getElementById("sidePanel").innerHTML = "";
    bookEntryLayout = document.getElementById("main").innerHTML;
    document.getElementById("main").innerHTML = "";
    filterContainerHTML = document.getElementById("filterContainer").innerHTML;
    document.getElementById("filterContainer").innerHTML = "";
    post(json, 'cgi-bin/userOffers.py',populate);
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
            container.style.height = "21.2130em";
            container.style.margin = "auto";
            container.style.padding = "0.5em";
            container.innerHTML = bookEntryLayout;
            container.getElementsByClassName("bookViewTitle")[0].innerText = element.book.title;
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