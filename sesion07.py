
simple = 'Mi cadena permite comillas "dobles" en una sola linea'
doble = "Mi cadena permite comillas 'simples' en una sola linea"
triple_simple = '''Mi cadena
permite contenido
en varias lineas y comillas "dobles"'''
triple_doble = """Mi cadena
permite contenido
en varias lineas y comillas 'simples'"""
print(simple)
print(doble)
print(triple_simple)
print(triple_doble)

#Convertir cualquier valor a cadena
entero = str(1)
flotante = str(1E-3)
hexadecimal = str(0xA)
booleano = str(True)
print(entero)
print(flotante)
print(hexadecimal)
print(booleano)
print(type(entero))
print(type(flotante))
print(type(hexadecimal))
print(type(booleano))

#Uso del backslash "\"
#print("El mensaje enviado fue: \"Hello, I\'m a message\"")
#print('El mensaje enviado fue: \"Hello, I\'m a message\"')

#Uso de la función input
#entrada = input('Ingrese un valor: ')
#print(entrada)
#print(type(entrada))

#entero = int(input('Ingrese un valor entero: '))
#print(entero, type(entero))

#flotante = float(input('Ingrese un valor flotante: '))
#print(flotante, type(flotante))

#booleano = bool(input('Ingrese un valor booleano: '))
#print(booleano, type(booleano))

#Manejo de indices
print('Indexado positivo')
fruta = 'banana'
print(fruta)
print(fruta[0])
print(fruta[5])

print('Indexado negativo')
fruta = 'banana'
print(fruta)
print(fruta[-1])
print(fruta[-3])

#Slicing
#sintaxis basica: secuencia[inicio:fin:paso]
print('Slicing')
ciudad = 'LaPaz-Bolivia'
print(ciudad)
print('Slicing con indices positivos')
print(ciudad[0:6])
print(ciudad[0:6:2])
print('Slicing con indices negativos')
print(ciudad[-10:-2])
print(ciudad[-10:-2:2])

print('Slicing sin indice inicial y final')
print(ciudad[:6])
print(ciudad[6:])
print('Slicing sin indice inicial ni final')
print(ciudad[:])
print(ciudad[::2])

print('Slicing con paso negativo')
print(ciudad[10:4:-1])
print(ciudad[10::-2])

#Concatenacion de una cadena
print('Concatenación de cadenas')
cadena1 = 'Hola'
cadena2 = 'Mundo'
concatenada = cadena1 + ' ' + cadena2
print(concatenada)

#Repeticion de una cadena
print('Repetición de cadenas')
cadena = '-#-'
repetida = cadena * 10
print(repetida)

#Longitud de cadena
print('Longitud de una cadena')
cadena = 'Hola Mundo :D'
longitud = len(cadena)
print(cadena)
print(longitud,type(longitud))

#metodos de cadenas
#notacion: cadena.funcion()

#Funcion upper()
print('funcion upper')
cadena = 'cadena inicial #1'
mayuscula = cadena.upper()
print(cadena)
print(mayuscula)

#Funcion lower()
print('funcion lower')
cadena = 'CADENA INICIAL #2'
minuscula = cadena.lower()
print(cadena)
print(minuscula)

#Funcion capitalize()
print('funcion capitalize')
cadena = 'Cadena INICIAL #3'
capital = cadena.capitalize()
print(cadena)
print(capital)

#Funcion title()
print('funcion Title')
cadena = 'CADENA inicial #4'
titulo = cadena.title()
print(cadena)
print(titulo)

#Funcion swapcase()
print('funcion swapcase')
cadena = 'CADena InIcIaL #5'
swap = cadena.swapcase()
print(cadena)
print(swap)

#Funcion count()
print('funcion count')
cadena = 'Cantidad de veces la letra A'
contar = cadena.count('a')
print(cadena)
print(contar, type(contar))

#Funcion find()
print('funcion find')
cadena = 'Encontrar las letras las'
buscar = cadena.find('las')
print(cadena)
print(buscar, type(buscar))

#Funcion rfind()
print('funcion rfind')
cadena = 'Encontrar las letras las'
buscar = cadena.rfind('las')
print(cadena)
print(buscar, type(buscar))

#Buscar numeros, alfabeticos y alfanumerico
print('funcion isdigit')
resultado = '100'.isdigit()
print(resultado,type(resultado))
print('funcion isaplha')
resultado = 'Hola'.isalpha()
print(resultado,type(resultado))
print('funcion isalnum')
resultado = 'usuario123'.isalnum()
print(resultado,type(resultado))

#funcion split
print('funcion split')
cadena = 'pan,carne,huevos'
separado = cadena.split(',')
print(cadena)
print(separado,type(separado))

#funcion join
print('funcion join')
cadena = 'abcdefghij'
unido = '-'.join(cadena)
print(cadena)
print(unido)

#funcion strip (util para la limpieza de datos en forms)
print('funcion strip')
cadena = '  Hola    Mundo   '
limpio = cadena.strip()
print(cadena)
print(limpio)
cadena = '-abc--def-ghi-cba----'
limpio = cadena.strip('bac-')
print(cadena)
print(limpio)

#funcion replace
print('Funcion replace')
cadena = 'Me gusta programar en JS, Amo JS'
reemplazado = cadena.replace('JS','Python')
print(cadena)
print(reemplazado)

#funcion format
print('funcion format')
cadena = 'El valor de PI es: {}'
formateado = cadena.format(3.1416)
print(cadena)
print(formateado)

#funcion format con indices
print('funcion format con indices')
cadena = '{2} es la suma de {0} y {1}'
valor1 = 5
valor2 = 3
resultado = valor1+valor2
formateado = cadena.format(valor1,valor2,resultado)
print(cadena)
print(formateado)

#funcion format con nombres (util para form. de inscrip.)
print('funcion format con nombres')
cadena = '{ciudad} es la capital de {pais}'
pais = 'Francia'
ciudad = 'Paris'
formateado = cadena.format(pais=pais, ciudad=ciudad)
print(cadena)
print(formateado)


# funcion format con f-string
print('Función format con f-string')
moneda = 'Boliviano'
pais = 'Bolivia'
formateado = f'La moneda de {pais} es el {moneda}'
print(formateado)







