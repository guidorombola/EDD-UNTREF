def sumaMatricesCuadradas(matriz1, matriz2):

    if not is_square(matriz1) or not is_square(matriz2) or not have_same_dimentions(matriz1, matriz2):
        return "Error de dimensiones de matrices"

    matriz_salida = [[matriz1[row][col] + matriz2[row][col] for col in range(len(matriz1))] for row in range(len(matriz1))]
    return matriz_salida


def is_square(matrix):
    es_cuadrada = True

    for i in range(len(matrix)):
        if len(matrix) != len(matrix[i]):
            es_cuadrada = False
    return es_cuadrada

def have_same_dimentions(matrix1, matrix2):

    same_dimentions = True
    if len(matrix1) == len(matrix2):
        for row in range(len(matrix1)):
            if len(matrix1[row]) != len(matrix2[row]):
                same_dimentions = False
    return same_dimentions

print(sumaMatricesCuadradas([[1,2],[3,4]], [[5,6],[7,8]]))