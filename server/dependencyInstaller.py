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
    import console_menu
except:
    Popen(['py','-m','pip','install','console-menu'])
