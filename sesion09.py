# Lista de enteros
print ("Lista de enteros")
mi_lista = [1,2,3,4,5]
print (mi_lista)

# Lista de cadenas
print ("Lista de cadenas")
mi_lista = ["hola", "mundo", "python"]
print (mi_lista)

# Lista mixta
print ("Lista mixta")
mi_lista = [1, "hola", 3.14, "mundo", 5]
print (mi_lista)

# Lista vacia
print ("Lista vacía")
mi_lista = []
print (mi_lista)

# Lista a partir de una cadena
print ("Lista a partir de una cadena")
mi_lista = list("hola mundo")
print (mi_lista)

# Lista a partir de una tupla
print ("Lista a partir de una tupla")
mi_tupla = (1,2,3,4,5)
print (mi_tupla)
mi_lista = list(mi_tupla)
print (mi_lista)

# Lista por comprensión
print ("Lista por comprensión")
mi_lista = [x for x in range(10)]
print (mi_lista)

# Indexación positiva de una lista
print ("Indexación positivo de una lista")
lista = [1, "hola", 3.14, (1,2)]
print (lista[0], type(lista[0])) 
print (lista[1], type(lista[1])) 
print (lista[2], type(lista[2])) 
print (lista[3], type(lista[3]))

# Indexación negativa de una lista


# Modificación de una lista
print ("Modificación de una lista")
lista = [1, "hola", 3.14, (1,2)]
print (lista)
lista[0] = 2
lista[1] = "mundo"
print (lista)

# Slicing de una lista
print ("Slicing de una lista")
lista = ["P", "y", "t", "h", "o", "n", "L", "a", "P", "a", "z"]
print (lista)
sub_lista = lista[2:7]
print (sub_lista)
print (type(sub_lista))

# Slicing con paso positivo
print ("Slicing con paso positivo")
lista = ["P", "y", "t", "h", "o", "n", "L", "a", "P", "a", "z"]
print (lista)
sub_lista = lista[0:8:3]
print (sub_lista)

# Slicing con paso negativo
print ("Slicing con paso negativo")
lista = ["P", "y", "t", "h", "o", "n", "L", "a", "P", "a", "z"]
print (lista)
sub_lista = lista[8:2:-4]
print (sub_lista)

# Slicing negativo con paso negativo 
print ("Slicing negativo con paso negativo")
lista = ["P", "y", "t", "h", "o", "n", "L", "a", "P", "a", "z"]
print (lista)
sub_lista = lista[-1:-8:-2]
print (sub_lista)

# Slicing negativo con paso positivo
print ("Slicing negativo con paso positivo")
lista = ["P", "y", "t", "h", "o", "n", "L", "a", "P", "a", "z"]
print (lista)
sub_lista = lista[-8:-1:2]
print (sub_lista)

# Concatenación de listas
print ("Concatenación de listas")
lista1 = [1,2,3]
lista2 = ["a","b","c"]
concatenar = lista1 + lista2
print (lista1, lista2)
print (concatenar)
print (type(concatenar))

# Repetición de listas
print ("Repetición de listas")
lista = [True, False]
repetir = lista * 3
print (lista)
print (repetir)
print (type(repetir))

# Metodo index()
print ("Método index(valor)")
lista = [1,True,3.14,"hola",5]
valor = "hola"
print (valor, lista.index(valor))
valor = 3.14
print (valor, lista.index(valor))

# Metodo count()
print ("Método count(valor)")
lista = [1,True,3.14,"hola",5, True, True, 3.140]
valor = True
print (valor, lista.count(valor))
valor = 3.14
print (valor, lista.count(valor))

# Metodo insert(i,valor)
print ("Método insert(i, valor)")
lista = [1,2,3,4,5]
print (lista)
lista.insert(2, "OwO")
print (lista)

# Metodo append()
print ("Método append(valor)")
lista = [1,2,3,4,5]
print (lista)
lista.append("(OwO=)")
print (lista)

# Metodo extend(iterable)
print ("Método extend(iterable)")
lista = [1,2,3]
print (lista)
lista.extend(":3")
print (lista)
lista.extend(["(¬_¬ )", "(O_O=)"])
print (lista)
lista.extend(("😅", "😎"))
print (lista)

# Metodo remove()
print ("Método remove(valor)")
lista = [1,2,"UwU",4,5, "UwU"]
print (lista)
lista.remove("UwU")
print (lista)

# Metodo pop(i)
print ("Método pop(i)")
lista = ["OwO",3,"UwU",5]
print (lista)
lista.pop(1)
print (lista)
print ("Método pop()")
lista.pop()
print (lista)

# Another example
print ("Método pop(i)")
lista = ["OwO",3,"UwU",5]
print (lista)
x = lista.pop(1)
print (lista, x)
print ("Método pop()")
lista.pop()
print (lista)

# Metodo clear()
print ("Método clear()")
lista = ["ewe","OwO","UwU"]
print (lista)
lista.clear()
print (lista)

# metodo sort()
print ("Método sort()")
lista = [3,1,5,2,4]
print (lista)
lista.sort()
print (lista)

# metodo sort(reverse)
print ("Método sort(reverse=)")
lista = [3,1,5,2,4]
print (lista)
lista.sort(reverse=True)
print (lista)

# Metodo reverse()
print ("Método reverse()")
lista = [3,1,5,2,4]
print (lista)
lista.reverse()
print (lista)

# Metodo copy()
print ("Método copy()")
lista = [3,1,5,2,4]
print (lista)
copia = lista.copy()
print (copia)
print (copia == lista)

# Funcion len()
print ("Función len()")
lista = [1,True,3.14,"🐍",5]
print (lista)
print (len(lista))

# Funcion max()
print ("Función max()")
lista = [1,2,3,4,5]
print (lista)
print (max(lista))
lista = ["a","b","c","d","e"]
print (lista)
print (max(lista))

# Funcion min()
print ("Función min()")
lista = [1,2,3,4,5]
print (lista)
print (min(lista))
lista = ["a","b","c","d","e"]
print (lista)
print (min(lista))

# Funcion sum()
print ("Función sum()")
lista = [1,2,3,4,5]
print (lista)
print (sum(lista))

# Comparacion de listas
print ("Comparación de listas")
lista = [1,2,3,4,5]
print (lista)
print (3 in lista)
print (6 in lista)
print (3 not in lista)
print (6 not in lista)
print ([1,2,3] in lista)

# Comparación de más listas
print ("Comparación de listas")
lista1 = [1,2,3,4,5]
lista2 = [1,2,3,4,5]
lista3 = [1,2]
print (lista1, lista2, lista3)
print (lista1 is lista2)
print (lista1 is not lista2)
print (lista3 is lista1)

# Listas anidadas
print ("Listas anidadas")
lista = [1,2,3,[4,5,6]]
print (lista)
print (type(lista))
valor_lista = lista[3]
print (valor_lista)
print (type(valor_lista))
valor = valor_lista[1]
print (valor)
print (type(valor))


































