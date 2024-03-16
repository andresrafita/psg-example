# Conjunto de enteros
print ("Conjunto de enteros")
conjunto = {1, 2, 3, 4, 5}
print(conjunto) 
print(type(conjunto))

# Conjunto de cadenas
print ("Conjunto de cadenas")
conjunto = {'🍕','🍔','🍟','🌭'}
print(conjunto)
print(type(conjunto))

# Conjunto mixto
print ("Conjunto mixto")
conjunto = {1, True, 3.14, '☕'}
print(conjunto)
print(type(conjunto))

# Conjunto vacio
print ("Conjunto vacío")
conjunto = set()
print(conjunto)
print(type(conjunto))

# Conjunto a partir de la cadena
print ("Conjunto a partir de la cadena")
cadena = 'Hola Mundo'
conjunto = set(cadena)
print(conjunto)
print(type(conjunto))

# Conjunto a partir de una tupla
print ("Conjunto a partir de una tupla")
tupla = (1, 2, 3, 4, 5, 5)
conjunto = set(tupla)
print(conjunto)
print(type(conjunto))

# Conjunto a partir de una lista
print ("Conjunto a partir de una lista")
lista = [True, False, 0, 1]
conjunto = set(lista)
print(conjunto)
print(type(conjunto))

# Conjunto por comprensión
conjunto = {x for x in '🍕🍔🍟🍕🍔🍟🍔🍟'}
print(conjunto)
print(type(conjunto))

# Indexacion y slicing
conjunto = {1,2,3,4,5}
print(conjunto[0]) #error

conjunto = {1,2,3,4,5}
print(conjunto[0:3]) #error

# Concatenacion de conjuntos
conjunto1 = {1,2,3}
conjunto2 = {4,5,6}
print(conjunto1 + conjunto2) #error

# Repeticion con conjuntos
conjunto = {1,2,3}
print(conjunto * 3) #error

# Métodos de conjuntos
# Adición
# Metodo add()
print ("Método add()")
conjunto = {'🍕','🍔','🍟','🌭'}
print (conjunto)
conjunto.add('🥗')
print(conjunto)

# Metodo update()
print ("Método update()")
conjunto = {'🍕','🍔','🍟','🌭'}
print (conjunto)
conjunto.update(['🥤','🍦'])
print(conjunto) 
conjunto.update('🍩🍪')
print(conjunto) 
conjunto.update(('🍫','🍬'))
print(conjunto)
conjunto.update({'🍭','🍮'})
print(conjunto)

# Eliminación
# Metodo remove()
print ("Método remove()")
conjunto = {'🍕','🍔','🍟','🌭'} 
print (conjunto)
conjunto.remove('🍔')
print(conjunto)
# conjunto.remove('🍔')
# print(conjunto)
# Key Error: '🍔'

# Metodo discard()
print ("Método discard()")
conjunto = {'🍕','🍔','🍟','🌭'}
print (conjunto)
conjunto.discard('🍔')
print(conjunto)
conjunto.discard('🍔')
print(conjunto)

# Metodo pop()
print ("Método pop()")
conjunto = {'🍕','🍔','🍟','🌭', '🥤','🍦'}
print (conjunto)
print(conjunto.pop())
print(conjunto)
print(conjunto.pop())
print(conjunto)

# Metodo clear()
print ("Método clear()")
conjunto = {'🍕','🍔','🍟','🌭'}
print (conjunto)
conjunto.clear()
print(conjunto)

# Operaciones con conjuntos
# Metodo union()
print ("Método union()")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print (conjunto1, conjunto2)
union = conjunto1.union(conjunto2)
print(union)

# Metodo intersection()
print ("Método intersection()")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print (conjunto1, conjunto2)
interseccion = conjunto1.intersection(conjunto2)
print(interseccion)

# Metodo difference()
print ("Método difference()")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print ("1:",conjunto1,"2:",conjunto2)
diferencia = conjunto1.difference(conjunto2)
print("1 y 2:",diferencia)
diferencia = conjunto2.difference(conjunto1)
print("2 y 1:",diferencia)

# Metodo symmetric_difference()
print ("Método symmetric_difference()")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print (conjunto1,conjunto2)
diferencia_simetrica = conjunto1.symmetric_difference(conjunto2)
print(diferencia_simetrica)

# Asignación con operadores
# Metodo interseccion_update()
print ("Método intersection_update()")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print (conjunto1, conjunto2)
conjunto1.intersection_update(conjunto2)
print(conjunto1)

#Metodo difference_update()
print ("Método difference_update()")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print ("1:",conjunto1,"2:",conjunto2)
conjunto1.difference_update(conjunto2)
print("1:",conjunto1,"2:",conjunto2)

# Metodo symmetric_difference_update()
print ("Método symmetric_difference_update()")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print (conjunto1, conjunto2)
conjunto1.symmetric_difference_update(conjunto2)
print(conjunto1)

# Búsqueda
# Metodo issubset()
print ("Método issubset()")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
conjunto3 = {'🍔','🍟'}
print (conjunto1, conjunto2,conjunto3)
# ¿El conjunto1 es subconjunto del conjunto2?
print(conjunto1.issubset(conjunto2))
# ¿El conjunto3 es subconjunto del conjunto1?
print(conjunto3.issubset(conjunto1))

# Metodo issuperset()
print ("Método issuperset()")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
conjunto3 = {'🍔','🍟'}
print (conjunto1, conjunto2,conjunto3)
# ¿El conjunto1 es superconjunto del conjunto2?
print(conjunto1.issuperset(conjunto2)) # C1 contiene a C2?
# ¿El conjunto1 es superconjunto del conjunto2?
print(conjunto1.issuperset(conjunto3)) # C1 contiene a C3?

# Metodo isdisjoint()
print ("Método isdisjoint()")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨'}
conjunto3 = {'🍔','🍟'}
print (conjunto1, conjunto2, conjunto3)
# ¿El conjunto1 es superconjunto del conjunto2?
print(conjunto1.isdisjoint(conjunto2)) # C1 contiene a C2?
# ¿El conjunto1 es superconjunto del conjunto2?
print(conjunto1.isdisjoint(conjunto3)) # C1 contiene a C3?

# Copia
# ASignacion por referencia
print ("Asignación por referencia")
conjunto = {'🍕','🍔','🍟','🌭'}
print (conjunto)
copia = conjunto
copia.add('🥗')
print(conjunto)
print(copia)

# Metodo copy()
print ("Metodo copy")
conjunto = {'🍕','🍔','🍟','🌭'}
print (conjunto)
copia = conjunto.copy()
copia.add('🥗')
print(conjunto)
print(copia)

# Funciones con conjunto
# Funcion len()
print ("Función len()")
conjunto = {'🍕','🍔','🍟','🌭'}
print (conjunto)
print(len(conjunto))

# Funcion max()
print ("Función max()")
conjunto = {1, 2, 3, 4, 5}
print (conjunto)
print (max(conjunto))
conjunto = {'🍕','🍔','🍟','🌭'}
print (conjunto)
print(max(conjunto))

# Funcion min()
print ("Función min()")
conjunto = {1, 2, 3, 4, 5}
print (conjunto)
print (min(conjunto))
conjunto = {'🍨','🍔','🍟','🍕'}
print (conjunto)
print(min(conjunto))

# Funcion sum()
print ("Función sum()")
conjunto = {1, 2, 3, 4, 5}
print (conjunto)
print (sum(conjunto))

# Operadores con conjuntos
# Adición |=
print ("Operador |=")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto3 = {'🍕','🍨'}
print (conjunto1, conjunto2)
conjunto1 |= conjunto2
print(conjunto1)

# Comparaciones
print ("Operador ==")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍔','🍟', '🥤'}
conjunto3 = {'🍕','🍨'}
print (conjunto1, conjunto2, conjunto3)
print(conjunto1 == conjunto2)
print(conjunto1 == conjunto3)

print ("Operador !=")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍔','🍟', '🥤'}
conjunto3 = {'🍕','🍨'}
print (conjunto1, conjunto2, conjunto3)
print(conjunto1 != conjunto2)
print(conjunto1 != conjunto3)

print ("Operador <")
conjunto1 = {'🍔','🍟'}
conjunto2 = {'🍔','🍟', '🥤'}
conjunto3 = {'🍕','🍨'}
print (conjunto1, conjunto2, conjunto3)
print(conjunto1 < conjunto2)
print(conjunto1 < conjunto3)

print ("Operador >")
conjunto1 = {'🍔','🍟','🥤','🍕'}
conjunto2 = {'🍔','🍟', '🥤'}
conjunto3 = {'🍕','🍨'}
print (conjunto1, conjunto2, conjunto3)
print(conjunto1 > conjunto2)
print(conjunto1 > conjunto3)

print ("Operador <=")
conjunto1 = {'🍔','🍟'}
conjunto2 = {'🍔','🍟'}
conjunto3 = {'🍕','🍨'}
print (conjunto1, conjunto2, conjunto3)
print(conjunto1 <= conjunto2)
print(conjunto1 <= conjunto3)

print ("Operador >=")
conjunto1 = {'🍔','🍟'}
conjunto2 = {'🍔','🍟'}
conjunto3 = {'🍕','🍨'}
print (conjunto1, conjunto2, conjunto3)
print(conjunto1 >= conjunto2)
print(conjunto1 >= conjunto3)

# Operaciones con conjuntos
print ("Operador |")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print (conjunto1, conjunto2)
union = conjunto1 | conjunto2
print(union)

print ("Operador &")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print (conjunto1, conjunto2)
interseccion = conjunto1 & conjunto2
print(interseccion)

print ("Operador ^")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print (conjunto1, conjunto2)
diferencia_simetrica = conjunto1 ^ conjunto2
print(diferencia_simetrica)

print ("Operador -")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print ("1:",conjunto1, "2:",conjunto2)
diferencia = conjunto1 - conjunto2
print("1 - 2:",diferencia)
diferencia = conjunto2 - conjunto1
print("2 - 1:",diferencia)

# Asignacion con operaciones
print ("Operador |= Unión")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print (conjunto1, conjunto2)
conjunto1 |= conjunto2
print(conjunto1)

print ("Operador &= Intersección")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print (conjunto1, conjunto2)
conjunto1 &= conjunto2
print(conjunto1)

print ("Operador -= Diferencia")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print ("1:",conjunto1, "2:",conjunto2)
conjunto1 -= conjunto2
print("1 - 2:",conjunto1)
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 -= conjunto1
print("2 - 1:",conjunto2)

print ("Operador ^= Diferencia")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print (conjunto1, conjunto2)
conjunto1 ^= conjunto2
print(conjunto1)

# Conjuntos inmutables
conjunto = frozenset({'🍔','🍕','🥗','🍟','🌭'})
print(conjunto)
print(type(conjunto))

# Conjuntos aninados
conjunto = {{'🍅','🍓','🍎'}, {'🍈','🍐','🍏'}} #TypeError: unhashable type: 'set'
print(conjunto)
print(type(conjunto))

































