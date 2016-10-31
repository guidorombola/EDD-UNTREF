import re

'''
2. (a) Escribir una expresión regular que acepta únicamente cadenas no vacías donde se alternan estrictamente letras a y

b: acepta a; ab; aba; abab; b; ba; bab y rechaza abb; baa; abba

(b) Escribir una expresión regular que acepte sólo cadenas binarias que contengan la subcadena 111.
'''

string = "a ab aba abab b ba bab abb baa abba"
match_a = re.findall(r'(?:\b(?:ab)+a*\b|\b(?:ba)+b*\b|\bb\b|\ba\b)', "a ab aba abab b ba hola bab abb aa bb baa abba")
print(match_a)

match_b = re.findall(r'\b[01]*1{3}[01]*\b', "holaa h10101111 010111101 111 919 01010111lalala 111010111100")
print(match_b)
