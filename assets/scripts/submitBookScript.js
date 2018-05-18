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
    }
    else if(isbn_length < 1) {
        $("#title-input").prop('disabled', false);
        $("#author-input").prop('disabled', false);
        $("#languages").prop('disabled', false);
        $("#topics").prop('disabled', false);
        $("#thumbanil-input").prop('disabled', false);
    }
    if(title_length >= 1 && isbn_length < 1) {
        $("#isbn-input").prop('disabled', true);
    }
    else if(title_length < 1) {
        $("#isbn-input").prop('disabled', false);
    }

}