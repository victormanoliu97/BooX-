var auth2 = null;
var profilePicture = "";
var currentUserApiKey = "";
var currentUserEmail = ""

function onGoogleSignIn(googleUser) {
    var profile = googleUser.getBasicProfile();
    currentUserApiKey = profile.getId();
    currentUserEmail = profile.getEmail();
    window.location.replace("user-panel.html");
  }
function onLoadGoogleAuthApi() {
    gapi.load('auth2', function() {
      auth2 = gapi.auth2.init().then(function() {
        console.log(gapi.auth2.getAuthInstance().isSignedIn.get())
        if (gapi.auth2.getAuthInstance().isSignedIn.get()) {
          console.log(gapi.auth2.getAuthInstance().currentUser.get().getBasicProfile())
          var profile = gapi.auth2.getAuthInstance().currentUser.get().getBasicProfile();
          currentUserApiKey = profile.getId();
          currentUserEmail = profile.getEmail();
          post({'email':currentUserEmail,'apiKey':currentUserApiKey},'cgi-bin/users.py',function(response){console.log(response)});
          console.log('Image URL: ' + profile.getImageUrl());
          profilePicture = "url("+profile.getImageUrl()+")";
          if(document.getElementById("profileImage")!=null)
          {
            document.getElementById("profileImage").style.backgroundImage = profilePicture;
          }
          
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