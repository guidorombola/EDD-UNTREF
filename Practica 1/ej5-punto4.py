def ordenaNumeros(list, k):

    menores=[]
    mayores=[]
    iguales=[]

    for x in list:
        if x < k:
            menores.append(x)
        elif x > k:
            mayores.append(x)
        else:
            iguales.append(x)

    return mayores, menores, iguales

print (ordenaNumeros([1,2,4,6,10,5,5],5))