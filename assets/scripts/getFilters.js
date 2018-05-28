function getFilters() {
    var topic = document.getElementById("genres").value;
    var language = document.getElementById("languages").value;
    var max_distance = document.getElementById("distance").value;

    var obj = new Object();
    obj.topic = topic;
    obj.language = language;
    obj.max_distance = max_distance;
    var json = JSON.stringify(obj);

    var jsonToSend = json;
    var destinationToSend = 'cgi-bin/reportsHandler.py?filter='

    function testFilter() { alert("Yey"); }

    post(jsonToSend, destinationToSend, testFilter);
}

