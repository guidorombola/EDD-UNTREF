from lxml import etree

'''Dado el documento 'recetario.xml' Escribir las siguientes consultas:'''

arbol = etree.parse("recetario.xml")


#1) Todas las recetas en la categoría Pescado que tengan Vino blanco como ingrediente;
a = arbol.xpath("//receta[categoria='Pescado']/ingredientes[ingrediente='Vino blanco']/..")
print("a)", a)

#2) Todas las recetas que lleven hasta 45 minutos
#(verificar que la unidad de tiempo sea minutos) de preparación;
b = arbol.xpath("//receta/informacion_general/tiempo[.<='45' and @unidad='minutos']/../..")
b1 = arbol.xpath("//receta[informacion_general/tiempo<='45']")
b1_modificado = arbol.xpath("//receta[informacion_general/tiempo/@unidad='minutos' and informacion_general/tiempo<='45']")
print("b)", b)
print("b) otra solucion: ", b1_modificado)
print('Otra manera para b) con mismo resultado', b1)

#3) Todas las recetas que se pueden preparar con 1 Besugo
#(verificar que la cantidad del ingrediente Besugo sea 1
#No esta bien. Si cambio cantidad de Besugo en la receta a 2 sigue andando porque dentro de esa receta encuentra
#un ingrediente que matchea con cantidad 1 y otro que matchea con Besugo (aunque no sea el mismo)
c = arbol.xpath("//receta/ingredientes[ingrediente/@cantidad='1' and ingrediente='Besugo']/..")
c_corregido = arbol.xpath("//ingrediente[@cantidad=1 and .='Besugo']/../..")
print(c_corregido)

#4) Todos los textos de los pasos número 1 de todas las recetas.
d = arbol.xpath("//receta/preparacion/paso[@numero='1']/text()")
print(d)

f = arbol.xpath("//ingrediente/@cantidad")
print(f)
