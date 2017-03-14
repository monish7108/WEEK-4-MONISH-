import xml.dom.minidom as m
doc = m.parse("books.xml")
valeurs = doc.getElementById("cooking")
#element = doc.createElement("SessionDetaild")
#element=doc.createTextNode("33390")
#valeurs.setAttribute("id","192")
#valeurs.appendChild(element)
#doc.writexml(open("simplexml.xml","w"))



for n in valeurs:
    for child in n.childNodes:
        print(child.nodeValue)