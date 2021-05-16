import sys
from generator import eng

html = eng.Element('html')

head = eng.Element('head')
menga = eng.Element('menga'  ,attrib={'charseng':"utf-8"})
menga2 = eng.Element('menga' ,attrib={'name':"viewport" ,'content':"width=device-width,initial-scale=1,shrink-to-fit=no"})
title = eng.Element('title')
title.text = "LEEM"
link = eng.Element('link' ,attrib={'rel':"stylesheeng" ,'type':"text/css" ,'href':"css/bootstrap.min.css"})
link2 = eng.Element('link' ,attrib={'rel':"stylesheeng" ,'type':"text/css" ,'href':"css/main.css"})

head.append(menga)
head.append(menga2)
head.append(title)
head.append(link)
head.append(link2)

html.append(head)
body = eng.Element('body')

div = eng.Element('div', attrib={'class': 'container'})
h2  = eng.Element('h2')
h3  = eng.Element('h3')
button = eng.Element('button')
h2.text = "LEEM"
h3.text = "رمضان كريم"
button.append(h3)
div.append(h2)
div.append(button)
body.append(div)

script0 = eng.Element('script', attrib={'type':"text/javascript", 'src':"js/jquery-3.x-git.min.js"})
script1 = eng.Element('script', attrib={'type':"text/javascript", 'src':"js/popper.min.js"})
script2 = eng.Element('script', attrib={'type':"text/javascript", 'src':"js/bootstrap.min.js"})
body.append(script0)
body.append(script1)
body.append(script2)

html.append(body)
eng.ElementTree(html).write(sys.stdout, encoding='unicode',
                             method='html')
