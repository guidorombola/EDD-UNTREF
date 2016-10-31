#Dada una cadena de texto, ordena las palabras que empiezan con vocales en un diccionario
def ordenador_palabras(texto):

    dicc={"a":[],"e": [],"i": [],"o": [],"u": []}
    vocales=["a","e","i","o","u"]

    lista = texto.split(", ")

    for x in lista:
        for i in vocales:
            if(x.startswith(i)):
                dicc[i].append(x)

        # if x.startswith("a"):
        #     dicc["a"].append(x)
        # if x.startswith("e"):
        #     dicc["e"].append(x)
        # if x.startswith("i"):
        #     dicc["i"].append(x)
        # if x.startswith("o"):
        #     dicc["o"].append(x)
        # if x.startswith("u"):
        #     dicc["u"].append(x)

    return dicc

print(ordenador_palabras("ana, enano, indio, oso, asado, ala"))
