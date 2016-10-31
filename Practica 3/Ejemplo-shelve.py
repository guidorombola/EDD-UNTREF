import shelve

def personas_en_estantes(archivo, lista):

    db=shelve.open(archivo)

    for p in lista:
        db[p.nombre]=p
    db.close()

def personas_desde_estantes(archivo):

    lista=[]
    db=shelve.open(archivo)

    for clave in db:
        lista.append(db[clave])

    return lista

class Persona:

    nombre=""

    def __init__(self, nombre):
        self.nombre = nombre

    def __repr__(self):
        return self.nombre