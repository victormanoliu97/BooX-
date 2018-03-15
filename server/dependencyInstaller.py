from subprocess import Popen
try:
    import cx_Oracle
except:
    Popen(['py','-m','pip','install','cx_Oracle'])