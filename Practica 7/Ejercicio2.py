from lxml import etree

tree = etree.parse("courses-noID - castellano.xml")
a = tree.xpath("//Titulo")
b = tree.xpath("//Departamento/Director//Apellido")
c = tree.xpath("//Materia[@Vacantes>'500']/Titulo")
d = tree.xpath("//Materia/Correlativas[Corre='CS106B']/../../Titulo")
e = tree.xpath("//Docentes//Segundo_Nombre/../Apellido")
f = tree.xpath("//Materia[@Vacantes>='100']/Docentes//Apellido")
for nodo in f:
    print(nodo.text)