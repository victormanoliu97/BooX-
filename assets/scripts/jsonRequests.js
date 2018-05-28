function post(json,destination,callback)
{
    var jsonField = "json=" + JSON.stringify(json);
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("POST", destination);
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200)
        {
            callback(this);
        }
    };
    xmlhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xmlhttp.send(jsonField);
}