# Description
This is a college project, its main purpose is to create a platform that intermediates exchange of books between book passionates

# Running the app
If you want to test the app locally you will need to follow these steps. Make sure that you have a python environment properly configured and an oracle database and server properly configured

###### 1. Clone the application : 
``` git clone https://github.com/victormanoliu97/BooX-.git ```

###### 2. Run the script to install all necesarily dependencies
``` cd server/ ```
``` python dependencyInstaller.py ```

###### 3. Populate your oracle database with topics 
``` python databaseManager.py ```

###### 4. Start the server 
``` python mainServer.py ```


# Arhitecture
The arhitecture used for this project is MVC(Model-View-Controller) , the functionality of the application being provided by implementing the REST paradigm
