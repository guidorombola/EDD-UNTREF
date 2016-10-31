class Cifrador(object):

    """Cifrador por sustitucion"""
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    alfabeto_cifrado = 'abcdefghijklmnopqrstuvwxyz'

    def __init__(self, clave="", tipo=""):

        """Las subclases pueden tener diferentes tipos de claves
         tipo es una cadena, por ejemplo "Caesar" """

        self.clave=clave
        self.tipo=tipo

    def __str__(self):
        """La representacion de un cifrador es su tipo"""
        return "Cifrador "+self.tipo

    def cifrar(self, frase):

        """Cifrado por sustitucion: reemplaza cada letra de la frase,
        por la correspondiente letra en el alfabeto cifrado """

        frase_cifrada=''

        for c in frase:
            i=self.alfabeto.find(c)
            if i != -1:
                frase_cifrada += self.alfabeto_cifrado[i]
            else:
                frase_cifrada += c
        return(frase_cifrada)

    def descifrar(self, frase_cifrada):

        """Descifra una frase cifrada, reemplazando cada caracter de
        la misma por el caracter correspondiente en el alfabeto """

        frase=''

        for c in frase_cifrada:
            i=self.alfabeto_cifrado.find(c)
            if i != -1:
                frase += self.alfabeto[i]
            else:
                frase += c

        return frase
