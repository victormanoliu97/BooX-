var auth2 = null;
function getUserGeoLocation() {
    if(navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(pos) {
            $("#location-id").css('color', 'rgba(216, 0, 50, 1)');
            var userLatitude = pos.coords.latitude;
            var userLongitude = pos.coords.longitude;

            var profile = gapi.auth2.getAuthInstance().currentUser.get().getBasicProfile();

            console.log("My test location is: " + userLongitude + " " + userLatitude);

            json = {};
            json.apikey = currentUserApiKey;
            json.latitude = userLatitude;
            json.longitude = userLongitude;

            put(json, 'cgi-bin/distanceHandler.py', sendCallback);
            console.log(json);
        });
    }
    else {
        alert("Error : geolocation is not supported");
    }
}

function sendCallback(json) {
    console.log(json);
    json = JSON.parse(json);

    if (json.type == 'error')
    {
        console.log("Nu am reusit sa fac put-ul pe locatie");
    }
    if (json.type == 'success')
    {
        console.log("Am reusit sa fac put-ul pe locatie");
    }
}

