var auth2 = null;
var profilePicture = "";

function onGoogleSignIn(googleUser) {
    var profile = googleUser.getBasicProfile();
    console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
    console.log('Name: ' + profile.getName());
    console.log('Image URL: ' + profile.getImageUrl());
    console.log('Email: ' + profile.getEmail()); // This is null if the 'email' scope is not present.
    window.location.replace("user-panel.html");
  }
function onLoadGoogleAuthApi() {
    gapi.load('auth2', function() {
      auth2 = gapi.auth2.init().then(function() {
        console.log(gapi.auth2.getAuthInstance().isSignedIn.get())
        if (gapi.auth2.getAuthInstance().isSignedIn.get()) {
          console.log(gapi.auth2.getAuthInstance().currentUser.get().getBasicProfile())
          var profile = gapi.auth2.getAuthInstance().currentUser.get().getBasicProfile();
          console.log('Image URL: ' + profile.getImageUrl());
          profilePicture = "url("+profile.getImageUrl()+")";
          
        }
        else
        {
          window.location.replace("index.html");
        }
      });
    });
    
  }
function signOut() {
  var auth2 = gapi.auth2.getAuthInstance();
    auth2.signOut().then(function () {
      console.log('User signed out.');
      window.location.replace("index.html");
    });
}