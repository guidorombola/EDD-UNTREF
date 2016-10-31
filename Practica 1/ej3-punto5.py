#Funcion que extrae la ultima palabra de un texto
def extraer_ultima_Palabra(texto):

    listapalabras=texto.split()
    ultimapalabra=listapalabras[-1]

    return "La ultima palabra del texto es: "+ultimapalabra

print(extraer_ultima_Palabra("En Estructuras de Datos usamos Python como lenguaje de programacion"))
