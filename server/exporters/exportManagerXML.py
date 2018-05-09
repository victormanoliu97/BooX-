import cx_Oracle
import os 
from io import StringIO
import lxml.etree
import lxml.builder
import xml.etree.cElementTree as ET

conn = cx_Oracle.connect('TW/TWBooX@localhost:1521')
cursor = conn.cursor()

from exportManager import getNumberOffers
from exportManager import getNumberOfGenres
from exportManager import getNumberOfLanguages
from exportManager import userReport

root = ET.Element("root")
doc = ET.SubElement(root, "user-report")

ET.SubElement(doc, "field1", name="genres-number").text = str(userReport[0])
ET.SubElement(doc, "field2", name="languages-number").text = str(userReport[1])
ET.SubElement(doc, "field3", name="offers-number").text = str(userReport[2])

tree = ET.ElementTree(root)
tree.write("../../assets/reports/report.xml")
    