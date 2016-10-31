#Dada una temperatura en grados farenheit, la devuelve convertida a celsius

def farenheit_a_celsius(temperatura_en_farenheit):
    return (temperatura_en_farenheit-32)*5/9

for i in range(0,120,10):
	print(farenheit_a_celsius(i))
