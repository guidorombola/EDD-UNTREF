from Persona import Persona

import shelve

class Agenda:

    def __init__(self):
        self.contactos = {}

    def agregar_contacto(self, nombre, email, telefono, domicilio):
        self.contactos[nombre] = Persona(nombre, email, telefono, domicilio)

    def modificar_contacto(self, persona, parametro_a_modificar, nuevo_valor):
        self.contactos[persona].parametro_a_modificar = nuevo_valor

    def existe_persona(self, nombre):
        return self.contactos.__contains__(nombre)

    def ver_datos(self, persona):
        return self.contactos.get(persona)

    def listar_personas(self):

        salida = ""

        for persona in self.contactos:
            salida += str(self.contactos.get(persona)) + " "

        return salida

    def shelf_contactos(self):

        db = shelve.open("estantes.s")

        for persona in self.contactos.values():
            db[persona.nombre] = persona
        db.close()

    def recuperar_contactos(self):

        dicc = {}

        db = shelve.open("estantes.s")

        for clave in db:
            dicc[clave] = db[clave]

        db.close()
        self.contactos = dicc

        return self.contactos

    def recuperar_un_contacto(self, nombre):

        db = shelve.open("estantes.s")
        contacto = db[nombre]
        db.close()
        return contacto