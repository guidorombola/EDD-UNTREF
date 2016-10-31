class Persona:

    def __init__(self, nombre, email, telefono, domicilio):

        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.domicilio = domicilio

        #self.datos = {"Nombre": nombre, "Email": email, "Telefono":telefono, "Domicilio": domicilio}

    def __repr__(self):
        return "Nombre: {0}, Email: {1}, Telefono: {2}, Domicilio: {3}".format(self.nombre, self.email,
                                                                                    self.telefono, self.domicilio)

    def __str__(self):
        return "Nombre: {0}, Email: {1}, Telefono: {2}, Domicilio: {3}".format(self.nombre, self.email,
                                                                                    self.telefono, self.domicilio)