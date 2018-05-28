function getFilters() {
    var topic = document.getElementById("genres").value;
    var language = document.getElementById("languages").value;
    var max_distance = document.getElementById("distance").value;

    json = {}
    json.topic = topic;
    json.language = language;
    json.max_distance = max_distance;

    var jsonToSend = json;
    var destinationToSend = 'cgi-bin/getBooks.py';

    function testFilter() { console.log(jsonToSend); }

    post(jsonToSend, destinationToSend, testFilter);
}

