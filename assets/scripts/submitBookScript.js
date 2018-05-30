var usingISBN = true;
var bookTopics = []
var interestedTopics = []
function validateForm() {
    
    var isbn_value = document.getElementById("isbn-input").value;
    var isbn_length = isbn_value.length;

    var title_value = document.getElementById("title-input").value;
    var title_length = title_value.length;

    var author_value = document.getElementById("author-input").value;
    var author_length = author_value.length;

    var languages_value = document.getElementById("languages").value;
    var languages_length = languages_value.length;

    var topics_value = document.getElementById("topics").value;
    var topics_length = topics_value.length;

    var thumbanil_value = document.getElementById("thumbanil-input").value;
    var thumbanil_length = thumbanil_value.length;


    if(isbn_length >= 1) {
        $("#title-input").prop('disabled', true);
        $("#author-input").prop('disabled', true);
        $("#languages").prop('disabled', true);
        $("#topics").prop('disabled', true);
        $("#thumbanil-input").prop('disabled', true);
        usingISBN = true;
    }
    else if(isbn_length < 1) {
        $("#title-input").prop('disabled', false);
        $("#author-input").prop('disabled', false);
        $("#languages").prop('disabled', false);
        $("#topics").prop('disabled', false);
        $("#thumbanil-input").prop('disabled', false);
        usingISBN = false;
    }
    if(title_length >= 1 &&author_length >= 1 &&languages_length >= 1 &&thumbanil_length >= 1 && bookTopics.length >=1 && isbn_length < 1) {
        $("#isbn-input").prop('disabled', true);
        usingISBN = false;
    }
    else if(title_length < 1 && author_length < 1 && languages_length < 1 && thumbanil_length < 1 && bookTopics.length < 1 ) {
        $("#isbn-input").prop('disabled', false);
        usingISBN = true;
    }
}
function addBookTopic()
{
    topic = document.getElementById('topics').value;
    console.log(topic)
    console.log(validateTopic(topic))
    console.log(document.getElementById('selectedTopics'))
    if(validateTopic(topic))
    {
        document.getElementById('topics').value = "";
        if (bookTopics.length == 0)
        document.getElementById('selectedTopics').innerHTML = document.getElementById('selectedTopics').innerHTML + ' ' + topic;
        else
        document.getElementById('selectedTopics').innerHTML = document.getElementById('selectedTopics').innerHTML + ', ' + topic;
        bookTopics.push(topic);
    }
}
function addIntrestedTopic()
{
    topic = document.getElementById('intrestedTopics').value;
    if(validateTopic(topic))
    {
        document.getElementById('intrestedTopics').value = "";
        if(interestedTopics.length == 0)
        document.getElementById('selectedIntrestedTopics').innerHTML = document.getElementById('selectedIntrestedTopics').innerHTML + ' ' + topic;
        else
        document.getElementById('selectedIntrestedTopics').innerHTML = document.getElementById('selectedIntrestedTopics').innerHTML + ', ' + topic;
        interestedTopics.push(topic);
    }
}
function send()
{
    var isbn_value = document.getElementById("isbn-input").value;
    var title_value = document.getElementById("title-input").value;
    var author_value = document.getElementById("author-input").value;
    var languages_value = document.getElementById("languages").value;
    var topics_value = document.getElementById("topics").value;
    var thumbanil_value = document.getElementById("thumbanil-input").value;
    var exipration_date_value = document.getElementById("expiration-date").value;
    
    json = {};
    if (usingISBN)
    {
        json.apiKey = currentUserApiKey;
        json.isbn = isbn_value;
        json.title = '';
        json.author = '';
        json.language = '';
        json.topics = '';
        json.thumbnail = '';
        json.interestedInTopics = interestedTopics;
        json.expirationDate = exipration_date_value;
    }
    else
    {
        json.apiKey = currentUserApiKey;
        json.isbn = '';
        json.title = title_value;
        json.author = author_value;
        json.language = languages_value;
        json.topics = bookTopics;
        json.thumbnail = thumbanil_value;
        json.interestedInTopics = interestedTopics;
        json.expirationDate = exipration_date_value;
    }
    post(json,'cgi-bin/postNewEntry.py',sendCallback);
}
function sendCallback(json)
{
    console.log(json);
    json = JSON.parse(json);
    document.body.innerHTML = '<h1 id="message">'+json.message+"</h1>";
    if (json.type == 'error')
    {
        document.getElementById("message").style.color = 'red';
    }
    if (json.type == 'success')
    {
        document.getElementById("message").style.color = 'green';
    }
}
function validateTopic(topic)
{
    return topics.indexOf(topic) > -1;
}
function validateLanguage(language)
{
    return languages.indexOf(language) > -1;
}

function init()
{
    onLoadGoogleAuthApi();
}