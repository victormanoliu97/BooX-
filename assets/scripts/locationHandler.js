function getUserGeoLocation() {
    if(navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(pos) {
            $("#location-id").css('color', 'rgba(216, 0, 50, 1)');
            var userLatitude = pos.coords.latitude;
            var userLongitude = pos.coords.longitude;
            console.log("My test location is: " + userLongitude + " " + userLatitude);
        });
    }
    else {
        alert("Error : geolocation is not supported")
    }
}

function getUserLatitude() {
    if(navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(pos) {
            var userLatitude = pos.coords.latitude;
        });
    }
    else {
        alert("Error : geolocation is not supported")
    }
    return userLatitude;
}

function getUserLongitude() {
    if(navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(pos) {
            var userLongitude = pos.coords.longitude;
        });
    }
    else {
        alert("Error : geolocation is not supported")
    }
    return userLongitude;
}

function calculateDistance(lon2, lat2) {
    var earthRadius = 6371e3;
    var dLat = (lat2 - getUserLatitude()).toRadians();
    var dLon = (lon2 - getUserLongitude()).toRadians();
    var lat1 = getUserLatitude().toRadians();
    var lat2 = lat2.toRadians();

    var a = Math.sin(dLat/2) * Math.sin(dLat/2) + Math.sin(dLon/2) * Math.sin(dLon/2) * Math.cos(lat1) * Math.cos(lat2); 
    var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a)); 

    var distance = R * earthRadius;

    return distance;
}
