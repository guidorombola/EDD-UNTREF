def aparicion_caracteres(texto):
    dicc={}
    for x in texto:
        apariciones = dicc.get(x,0)
        dicc[x]=apariciones+1
    return dicc


print(aparicion_caracteres("Esto es un ensayo"))