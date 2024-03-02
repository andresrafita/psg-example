# 2. Escribe un programa en Python que convierta las siguientes temperaturas de grados Celsius a grados Fahrenheit:
# 30 ºC
# -273.99 ºC
# 100 ºC

def celsius_a_fahrenheit(celsius):
#formula F = C * (9/5) + 32
    return (celsius * 9/5) + 32
temperaturas_celsius = [30, -273.99, 100]
for temp_c in temperaturas_celsius:
    temp_f = celsius_a_fahrenheit(temp_c)
    print(f"{temp_c} ºC == {temp_f} ºF")
