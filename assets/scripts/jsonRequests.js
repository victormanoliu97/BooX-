function post(json,destination,callback)
{
    var jsonField = "?json=" + JSON.stringify(json);
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("POST", destination+jsonField);
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200)
        {
            callback(this.response);
        }
    };
    xmlhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xmlhttp.send(jsonField);
}
function get(json,destination,callback)
{
    var jsonField = "?json=" + JSON.stringify(json);
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", destination+jsonField);
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200)
        {
            callback(this.response);
        }
    };
    xmlhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xmlhttp.send(jsonField);
}
function put(json,destination,callback)
{
    var jsonField = "?json=" + JSON.stringify(json);
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("PUT", destination+jsonField);
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200)
        {
            callback(this.response);
        }
    };
    xmlhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xmlhttp.send(jsonField);
}
function del(json,destination,callback)
{
    var jsonField = "?json=" + JSON.stringify(json);
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("DELETE", destination+jsonField);
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200)
        {
            callback(this.response);
        }
    };
    xmlhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xmlhttp.send(jsonField);
}