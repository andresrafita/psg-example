# 5. Eres NOE y tienes que guardar dos animales de cada especie en un arca, crea un diccionario con las especies:
# arca = {"perro":2, "gato":2, "tigre":2, "mono":2, "unicornio":0, "jirafa":1}
# Añade al arca 2 especies mas usando update()
# Toma la lista de los animales en el arca iterando el diccionario
# Existe en el arca la especie 'dragon'?
# Elimina la especie 'unicornio' del arca
# Modifica el valor de la especie 'jirafa' por 2
# Vacia el arca despues del diluvio

arca = {"perro": 2, "gato": 2, "tigre": 2, "mono": 2, "unicornio": 0, "jirafa": 1}
arca.update({"elefante": 2, "oso": 2})
animales_en_arca = [animal for animal, cantidad in arca.items() for _ in range(cantidad)]
existe_dragon = 'dragon' in arca
del arca['unicornio']
arca['jirafa'] = 2
arca.clear()
print("Lista de animales en el arca:", animales_en_arca)
print("Existe la especie dragon:", existe_dragon)
print("Arca después del diluvio:", arca)





