#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
import re
import time
import sys

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}

def getTitle(link):
  req = urllib2.Request(link, headers=hdr)
  html = urllib2.urlopen(req)
  s_html= html.read()
  title_regex = re.search(r'<title>(.*)</title>', s_html, re.IGNORECASE)
  title = title_regex.group(0)
  title = title[7:-8]
  return title

def getLabel(line):
    label_regex = re.search(r'(.*);', line, re.IGNORECASE)
    label = label_regex.group(0)
    label = label[:-1]
    return label

def getURL(line,label):
    url = line[len(label)+1:-1]
    return url

#Añade el el caracter de escape \ delante de los caracteres especiales.
def fixURL(url):
    url.replace("#","\#")
    url.replace("_","\_")
    url.replace("&","\&")
    return url

def genItem(line):
    label = getLabel(line)
    url = getURL(line,label)
    date = time.strftime("%d/%m/%Y")
    title = getTitle(url)
    url = fixURL(url)

    item = "@misc{" + label + ",\n\tauthor = {},\n\ttitle = {" + title +"},\n\tyear = {(Accedido el "\
    + date + ")}, \n\thowpublished =\"\\url{"+url+"}\"\n} \n\n"
    return item

def genItem2(line):
    label = getLabel(line)
    url = getURL(line,label)
    date = time.strftime("%d/%m/%Y")
    url = fixURL(url)

    item = "@misc{" + label + ",\n\tauthor = {},\n\ttitle = {},\n\tyear = {(Accedido el "\
    + date + ")}, \n\thowpublished =\"\\url{"+url+"}\"\n} \n\n"
    return item

if(len(sys.argv) == 3):
    urls = open(sys.argv[1],"r")
    bib = open(sys.argv[2],"a")

    for line in urls:
        try:
            bib.write(genItem(line))
        except Exception:
            sys.exc_clear()
            bib.write(genItem2(line))
            print ("Linea -> " + line + " generada sin titulo" )

    urls.close()
    bib.close()

else:
    print ("Uso: ./bib_gen.py archivo_urls archivo_bib")
