from lxml import etree

tree = etree.parse('archivo.xml') #archivo.xml: pto 1 de la practica
root = tree.getroot() #Devuelve la raiz del arbol XML
# len(root) #los elementos del arbol son listas
# for child in root:
#     print(child)
#
# for child in root:
#     print(child.tag) #con .tag se accede a la etiqueta

b1 = tree.xpath("/Pedidos/Pedido/PC") #Devuelve todos los nodos PC que sean hijos de Pedido

b2 = tree.xpath("//Cliente//*") #Devuelve todos los nodos descendientes de clientes (en nuestro caso nada porque no hay
                                #nodos hijos, solo texto

b3 = tree.xpath("/Pedidos/Pedido[Cliente='Ana']") #Devuelve todos los nodos pedido en donde el cliente sea Ana

b4 = tree.xpath("//Pedido[Cliente and PC]/PC")  #Devuelve todos los nodos PC de los pedidos que tengan etiquetas
                                                #cliente y pc

b5 = tree.xpath("//*//Pedido[Cliente='Ana']/Cliente")   #De todos los descendientes de la raiz, para aquellos cuyo
                                                        #Cliente sea Ana, devuelve el nodo cliente

b6 = tree.xpath("//Pedido[Cliente='Juan'][PC != 'pc600']")  #Devuelve todos los nodos pedido que tengan como cliente
                                                            #a Juan y pc diferente de pc600 (en este caso no hay)

b7 = tree.xpath("//Pedido[PC='pc600']/*")   #Devuelve todos los nodos descendientes de Pedido que tengan 'pc600'


for nodo in b7:
    #print("Etiqueta: " + nodo.tag, "Texto: " + nodo.text)
    print(nodo)





