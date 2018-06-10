function searchWithFilters() {
    
    var topic = '';
    var language = '';
    var max_distance = '';
    var search = document.getElementById("search-bar").value;
    try {
        topic = document.getElementById("topics").value;
        language = document.getElementById("languages").value;
        max_distance = document.getElementById("distance").value;
    } catch (error) {
    }

    json = {};
    json.apikey = currentUserApiKey;
    json.search = search;
    json.topic = topic;
    json.language = language;
    json.distance = max_distance;

    var jsonToSend = json;
    var destinationToSend = 'cgi-bin/getBooks.py';

    ok0 = false;
    ok1 = false;
    if (validateTopic(topic)) ok1 = true;
    if (validateLanguage(language)) ok2 = true;
    console.log('done validating');
    if(ok1&&ok2)
    {
        console.log('sending');
        get(jsonToSend, destinationToSend, populate);
    }
}

function validateTopic(topic)
{
    if (topic.length == 0) return true;
    return topics.indexOf(topic) > -1;
}
function validateLanguage(language)
{
    if (language.length == 0) return true;
    return languages.indexOf(language) > -1;
}