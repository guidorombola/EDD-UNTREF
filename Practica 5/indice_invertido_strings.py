def indice_invertido_strings(lista_de_strings):

    inverted_index = {}

    for string in lista_de_strings:
        normalizado = string.lower()
        tokenizado = normalizado.split()
        indice = lista_de_strings.index(string)
        lista = inverted_index.setdefault(indice, [])
        for palabra in tokenizado:
            lista.append(palabra)

    return inverted_index

print(indice_invertido_strings(["Hola mauro","Como","Estas querido","guido","hola"]))