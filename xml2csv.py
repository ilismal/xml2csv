#!/usr/bin/python
# coding=utf-8
# -*- coding : utf-8 -*-

import urllib2
import xml.etree.ElementTree as ET
ficheroXML = urllib2.urlopen("https://server.local/XML/types.xml")
salida = open('temp.xml','wb')
salida.write(ficheroXML.read())
salida.close()
arbol = ET.parse('temp.xml')
raiz = arbol.getroot()
tipos = open('tipos.csv','wb')
tipos.write("Type;Boss;BK\n")
for request in raiz.iter('request_subtype'):
    tipos.write(request.find('type').text.encode("utf-8") + ";" + request.find('boss').text + ";" + request.find('bk').text + "\n")
tipos.close()
