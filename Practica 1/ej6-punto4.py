#Dada una matriz de n*n, devuelve cada columna en una lista

def matriz_a_listas(matrix):

    for i in range(len(matrix)):
        if len(matrix) != len(matrix[i]):
            return "Matriz no cuadrada"

    lista1 = [x[0] for x in matrix]
    lista2 = [x[1] for x in matrix]
    lista3 = [x[2] for x in matrix]
    return lista1, lista2, lista3

print(matriz_a_listas([[1,2,3],[4,5,6],[7,8,9]]))