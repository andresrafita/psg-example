# 3. Crea un diccionario con las siguientes tuplas de animales:
# tupla = (('perro','🐶'),('gato','😺'),('aves',['🐦','🦅']))
# Del diccionario obten y elimina el valor de la clave 'aves'
# Modifica el valor de la clave 'gato' por '🐈'
# Cambia la clave perro por perros y su valor por ['🐶','🐕']

diccionario = dict((('perro', '🐶'), ('gato', '😺'), ('aves', ['🐦', '🦅'])))
aves = diccionario.pop('aves', None)
diccionario['gato'] = '🐈'
diccionario['perros'] = diccionario.pop('perro', None)
diccionario['perros'] = ['🐶', '🐕']
print("Diccionario actualizado:", diccionario)



