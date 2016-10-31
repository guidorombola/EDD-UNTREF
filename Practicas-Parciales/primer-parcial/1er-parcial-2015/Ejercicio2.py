import pickle

def convertir_matriz_ady_a_dicc(matriz):
    dicc = {}
    if not es_cuadrada(matriz):
        return "La matriz no es cuadrada"
    for fila in range(len(matriz)):
        for col in range(len(matriz[fila])):
            lista = dicc.setdefault(fila+1, [])
            if matriz[fila][col] != 0:
                lista.append((col+1, matriz[fila][col]))
    return dicc

def es_cuadrada(matriz):
    cant_filas = len(matriz)
    cuadrada = True
    for fila in matriz:
        if len(fila) != cant_filas:
            cuadrada = False
    return cuadrada

def grados_ent(matriz):
    dicc = {}
    for fila in range(len(matriz)):
        for col in range(len(matriz[fila])):
            dicc.setdefault(col+1, 0)
            if matriz[fila][col] != 0:
                dicc[col+1] +=1
    return dicc

def guardar_grafo_en_disco(lista_ady, nombre_archivo):
    with open(nombre_archivo, "wb") as arch:
        pickle.dump(lista_ady, arch)

def mostrar_grafo(nombre_archivo):
    with open(nombre_archivo,"rb") as archivo:
        dicc = pickle.load(archivo)
    return dicc

def mostrar_como_lista(lista_ady):
    salida = ""
    for nodo in lista_ady.keys():
        salida+="Nodo "+str(nodo)+"\n"
        for item in lista_ady[nodo]:
            salida+="Vertice destino: {0}, Costo: {1}\n".format(item[0], item[1])
        salida+="\n"
    return salida

if __name__ == '__main__':
    matriz_de_adyacencia = [[0,1,2,0,0],[0,0,0,3,0],[0,0,0,0,4],[0,0,0,0,5],[0,0,0,0,0]]
    lista = convertir_matriz_ady_a_dicc(matriz_de_adyacencia)
    guardar_grafo_en_disco(lista, "lista1.p")
    print(mostrar_grafo("lista1.p"))
    print(mostrar_como_lista(lista))


