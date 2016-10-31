#Dada una matriz, devuelve los elementos de su diagonal en una lista
def diagonal(matrix):

   #Forma comprensiva
   return [matrix[i][i] for i in range(0, len(matrix[0]))]

    # Forma imperativa
    # lista=[]
    # for i in range(0,len(matrix[0])):
    #     lista.append(matrix[i][i])
    #
    # return lista

matrix=[[1,2,3],[4,5,6],[7,8,9],[20,11,15]]
print(diagonal(matrix))