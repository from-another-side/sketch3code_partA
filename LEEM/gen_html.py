import sys
from xml.etree import ElementTree as ET

html = ET.Element('html')

head = ET.Element('head')
meta = ET.Element('meta'  ,attrib={'charset':"utf-8"})
meta2 = ET.Element('meta' ,attrib={'name':"viewport" ,'content':"width=device-width,initial-scale=1,shrink-to-fit=no"})
title = ET.Element('title')
title.text = "LEEM"
link = ET.Element('link' ,attrib={'rel':"stylesheet" ,'type':"text/css" ,'href':"css/bootstrap.min.css"})
link2 = ET.Element('link' ,attrib={'rel':"stylesheet" ,'type':"text/css" ,'href':"css/main.css"})

head.append(meta)
head.append(meta2)
head.append(title)
head.append(link)
head.append(link2)

html.append(head)


body = ET.Element('body')

div = ET.Element('div', attrib={'class': 'container'})
h2 = ET.Element('h2')
h3 = ET.Element('h3')
button = ET.Element('button')
h2.text = "LEEM"
h3.text = "رمضان كريم"
button.append(h3)
div.append(h2)
div.append(button)
body.append(div)

script0 = ET.Element('script', attrib={'type':"text/javascript", 'src':"js/jquery-3.x-git.min.js"})
script1 = ET.Element('script', attrib={'type':"text/javascript", 'src':"js/popper.min.js"})
script2 = ET.Element('script', attrib={'type':"text/javascript", 'src':"js/bootstrap.min.js"})
body.append(script0)
body.append(script1)
body.append(script2)


html.append(body)

ET.ElementTree(html).write(sys.stdout, encoding='unicode',
                             method='html')
