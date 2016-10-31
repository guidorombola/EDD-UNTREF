def devuelve_transpuesta(matrix):
    transpuesta=matrix

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            transpuesta[row][col] = matrix[col][row]

    return matrix

print(devuelve_transpuesta([[4,1,3],[2,5,4],[1,3,4]]))