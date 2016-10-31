import re

'''Escribir un programa Python que maneje expresiones regulares y que encuentre y reemplace dentro de un texto todos
los nombres de usuarios de twitter por la palabra USER (los usuarios de twitter comienzan con @ seguido de letras y
números, por ejemplo: @usuario21). Se debe tener cuidado de no atrapar y reemplazar direcciones de correo
electrónico con la forma usuario@dominio'''

string = "@pepe32 @12345 algo@hotmail.com @reg_ex rx_a@gmail.com"

salida = re.sub(r"(?<!\w)@\w+", "USER", string)
print(salida)


'''
Una dirección MAC (de placa de red) es una dirección formada por 6 bloques hexadecimales de 2 dígitos cada uno,
separados por : o por - (a) Escribir una expresión regular que acepte sólo direcciones MAC válidas. Solo debe aceptar
direcciones que usan el mismo separador. Por ejemplo 00:1F:A1:cC:11:9e es válida pero no 00-1F:A1- cC:11:9e . (b)
Escribir una expresión regular que acepta sólo direcciones MAC capicúas que se lean exactamente igual (por ejemplo
debe aceptar 00:1F:2A:A2:F1:00 pero no 00:1F:2A:2A:1F:00).
'''

string2 = "AA:00:BF:2C:22:F5 00:1F:2A:A2:F1:00 hola"
salida_a = re.findall(r'(?:(?:[A-Fa-f\d]{2}):){5}(?:[A-Fa-f\d]){2}', string2)
salida_b = re.search(r'([A-F]|[0-9])([A-F]|[0-9]):([A-F]|[0-9])([A-F]|[0-9]):([A-F]|[0-9])([A-F]|[0-9]):\6\5:\4\3:\2\1', string2)
salida_a_modificada = re.findall(r'[A-Fa-f0-9]{2}([:-])(?:[0-9a-fA-F]{2}\1){4}[0-9A-Fa-f]{2}', string)
salida_b_modificada = re.findall(r'([0-9A-Fa-f])([0-9A-Fa-f])([:-])([0-9A-Fa-f])\4\3\2\1',string) #No esta completa
print("a)", salida_a_modificada)
print("b)", salida_b)
