#!/usr/bin/python
import os
import sys
import cgi
import re
import cgitb; cgitb.enable() # Optional; for debugging only
sys.path.append('../server')
import GoogleBooksApiHandler as GBooks
import languages as Lang
from pprint import pprint

def sendReport(format):
    with open('reports/report.{format}'.format(format=format)) as file:
        for line in file.readlines():
            print(line)


arguments = cgi.FieldStorage()

if 'format' not in arguments.keys():
    print("Content-Type: text/html\n")
    print("<error>No selected format</error>")
    exit(0)
format = arguments['format'].value

if format=='html':
    print("Content-Type: text/html\r")
    print('Content-Disposition: attachment; filename="report.html"\r\n')
    sendReport('html')
elif format=='json':
    print("Content-Type: application/json\r")
    print('Content-Disposition: attachment; filename="report.json"\r\n')
    sendReport('json')
elif format=='xml':
    print("Content-Type: application/xml\r")
    print('Content-Disposition: attachment; filename="report.xml"\r')
    sendReport('xml')
else:
    print("Content-Type: text/html\n")
    print("<error>Invalid Format</error>")