from xml.dom import minidom

xmldoc=minidom.parse("staff.xml")

#print(xmldoc.toprettyxml())

name=xmldoc.getElementsByTagName("name")[0]

print(name.firstChild.data)

node = xmldoc.createElement('staff')
node.setAttribute("id","1007")
nodetext=xmldoc.createTextNode("hello")

node.appendChild( nodetext  )
xmldoc.childNodes[0].appendChild( node )


staffs = xmldoc.getElementsByTagName("staff")
for staff in staffs:
        sid = staff.getAttribute("id")
        nickname = staff.getElementsByTagName("nickname")[1]
        salary = staff.getElementsByTagName("salary")[0]
        print("id:%s, nickname:%s, salary:%s" %
              (sid, nickname.lastChild.data, salary.firstChild.data))