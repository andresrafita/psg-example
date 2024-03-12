#Tuplas de enteros
enteros = (1,2,3,4,5,6)
print(enteros)
print(type(enteros))

#Tuplas de cadenas
cadenas = ('hola','mundo','desde','python')
print(cadenas)
print(type(cadenas))

#Tupla mixta
mixta = (1,'hola',True,2.5)
print(mixta)
print(type(mixta))

#Tupla vacia
vacia = ()
print(vacia)
print(type(vacia))

# Tupla de un solo elemento
uno = (1,)
print(uno)
print(type(uno))

# Tupla usando funcion tuple()
constructor = tuple('hola')
print(constructor)
print(type(constructor))

# Indexing and Slicing
# Indexado positivo de tupla
tupla = (1,2.0,'hola',True)
print(tupla[0], type(tupla[0]))
print(tupla[1], type(tupla[1]))
print(tupla[2], type(tupla[2]))
print(tupla[3], type(tupla[3]))

# Indexado negativo de tupla
tupla = (1,2.0,'hola',True)
print(tupla[-1], type(tupla[-1]))
print(tupla[-2], type(tupla[-2]))
print(tupla[-3], type(tupla[-3]))
print(tupla[-4], type(tupla[-4]))

#Slicing de una tupla
tupla = (0,1,2,3,4,5,6,7,8,9,10)
print(tupla)
sub_tupla = tupla[0:5]
print(sub_tupla)
print(type(sub_tupla))

#Slicing de una tupla con pasos positivos
tupla = (0,1,2,3,4,5,6,7,8,9,10)
print(tupla)
sub_tupla = tupla[0:10:2]
print(sub_tupla)
print(type(sub_tupla))

#Slicing de una tupla con pasos negativos
tupla = (0,1,2,3,4,5,6,7,8,9,10)
print(tupla)
sub_tupla = tupla[7:2:-2]
print(sub_tupla)
print(type(sub_tupla))

#Concatenacion de tuplas
tupla1 = (1,2,3)
tupla2 = (4,5,6)
concatenar = tupla1 + tupla2
print(tupla1,tupla2)
print(concatenar)
print(type(concatenar))

#Repeticion de tuplas
tupla = (1,2,3)
repetir = tupla * 3
print(tupla)
print(repetir)
print(type(repetir))

#Asignacion multiple
persona = ('Jhon','Doe',22,1.75)
nombre,apellido,edad,estatura = persona
print(persona)
print(nombre)
print(apellido)
print(edad)
print(estatura)

#Metodo index(valor)
tupla = (1,2.0,'hola',True)
print(tupla.index(2.0))
print(tupla.index('hola'))

#Metodo count(valor)
tupla = (1,2.0,'hola',False,'hola','HOLA')
print(tupla.count(1))
print(tupla.count('hola'))
print(tupla.count(10))

#Funcion len()
tupla = (1,2.0,'hola',True)
longitud = len(tupla)
print(tupla)
print(longitud)

#Funcion max()
tupla = (1,2,10,5,8,0)
maximo = max(tupla)
print(tupla)
print(maximo)

#Funcion min()
tupla = ('a','z','c','b','f','d')
minimo = min(tupla)
print(tupla)
print(minimo)

#Funcion sum()
tupla = (1.0,0.5,2.5,3.1)
suma = sum(tupla)
print(tupla)
print(suma)

#Tuplas anidadas
tupla = (1,2,3, (4,5,6))
print(tupla)
print(tupla,type(tupla))
print(tupla[3],type(tupla[3]))
print (tupla[3][0],type(tupla[3][0]))

#Anidado al detalle
tupla = (1,2,3, (4,5,6))
print(tupla,type(tupla))
anidado = tupla[3]
print(anidado,type(anidado))
valor_anidado_0 = anidado[0]
print(valor_anidado_0,type(valor_anidado_0))
valor_anidado_1 = tupla[3][1]
print(valor_anidado_1,type(valor_anidado_1))






