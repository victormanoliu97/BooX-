from subprocess import Popen
from time import sleep
import os

running = True

while running:
    sleep(30)
    if os.path.isfile(os.path.join(os.path.dirname(__file__),'exportManagerHTML.py')):
        htmlReportProcess = Popen(['python','exportManagerHTML.py'])
    if os.path.isfile(os.path.join(os.path.dirname(__file__),'exportManagerXML.py')):
        htmlReportProcess = Popen(['python','exportManagerXML.py'])
    if os.path.isfile(os.path.join(os.path.dirname(__file__),'exportManagerJSON.py')):
        htmlReportProcess = Popen(['python','exportManagerJSON.py'])

def close():
    running = False
