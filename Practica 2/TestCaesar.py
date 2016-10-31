import caesar
import unittest
import random

class TestCaesar(unittest.TestCase):

    def setUp(self):
        self.frases=['Rosita Wachenchauzer', 'estructura de datos', 'Martin Albarracin' ]
        self.cifradas3=['Rrvlwd Wdfkhqfkdxchu','hvwuxfwxud gh gdwrv','Mduwlq Aoeduudflq']

    def test_clave_cero(self):
        """Asegurarse que con clave 0 nos da la misma frase"""
        for f in self.frases:
            self.assertEqual(caesar.cifrar(f,0), f)

    def test_cifrar(self):
        """Asegurarse que cifra bien frases (sin normalizar) conocidas"""

        clave=3

        for i in range(len(self.frases)):
            self.assertEqual(caesar.cifrar(self.frases[i], clave), self.cifradas3[i])

    def test_descifrar(self):

        """Asegurarse que si ciframos y desciframos con la misma clave
        se obtiene de nuevo la frase original """

        clave = random.randint(0,26)

        for f in self.frases:
            frase_cifrada=caesar.cifrar(f,clave)
            self.assertEqual(caesar.descifrar(frase_cifrada, clave), f)


if __name__ == '__main__':
    unittest.main

