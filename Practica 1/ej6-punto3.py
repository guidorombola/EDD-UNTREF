#Dado un entero n, crea una matriz identidad de n*n
def generador_identidad(tamanio):

    identidad=[]

    # Forma Imperativa

    # for row in range(0, tamanio):
    #     tmp=[]
    #     for col in range(0, tamanio):
    #         if row == col:
    #             tmp.append(1)
    #         else:
    #             tmp.append(0)
    #     identidad.append(tmp)

    #Por comprension

    identidad = [[1 if row == col else 0 for col in range(tamanio)] for row in range(tamanio)]

    return identidad

print (generador_identidad(3))