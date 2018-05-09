from subprocess import Popen
from time import sleep

running = True

while running:
    sleep(30)
    htmlReportProcess = Popen(['python','exportManagerHTML.py'])
    htmlReportProcess = Popen(['python','exportManagerXML.py'])
    htmlReportProcess = Popen(['python','exportManagerJSON.py'])

def close():
    running = False
