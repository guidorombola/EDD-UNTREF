#Extrae una palabra de un texto y la almacena en una variable

def extractor(texto, palabraDeseada):

   longitud = len(palabraDeseada)
   posicion = texto.find(palabraDeseada)

   if posicion < 0:
       return "La palabra no se encuentra en el texto"
   else:
       extraccion=texto[posicion:posicion+longitud]
       return extraccion

print(extractor("En Estructuras de Datos usamos Python como lenguaje de programacion", "Datos"))