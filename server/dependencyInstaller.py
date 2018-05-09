from subprocess import Popen
try:
    import cx_Oracle
except:
    Popen(['py','-m','pip','install','cx_Oracle'])
try:
    import json
except:
    Popen(['py','-m','pip','install','json'])
try:
    import consolemenu
except:
    Popen(['py','-m','pip','install','console-menu'])
try:
    import oauth2client
except:
    Popen(['py','-m','pip','install','google-api-python-client'])
try:
    import plotly as py 
except:
    Popen(['py','-m', 'pip', 'install', 'plotly'])
try:
    from lxml import etree
except:
    Popen(['py','-m', 'pip', 'install', 'lxml'])
