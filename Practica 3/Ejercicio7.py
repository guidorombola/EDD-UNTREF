import pickle

class Agenda(object):

    contactos = []

    def agregar_contacto(self, nombre, tel="", email="", domicilio=""):
        self.contactos.append((nombre,{"tel": tel, "email": email, "domicilio": domicilio}))

    def guardar_contactos(self):
        pickle.dump(self.contactos, open("agenda.p","wb"))

    def recuperar_contactos(self):
        self.contactos = pickle.load(open("agenda.p","rb"))


if __name__ == "__main__":
    a = Agenda()
    a.agregar_contacto("Juan Perez", tel={"casa": "4517-9165", "cel":"15-4278-7240"}, email=["juan@gmail.com", "juanjo@untref.edu.ar"], domicilio= {"calle": "Urquiza", "Nro": "1467","Piso":"6", "Depto": "B", "localidad": "Caseros"})
    print(a.contactos)