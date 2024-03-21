# 2. Crea un diccionario para almacenar información de comidas de animales por ejemplo:
# comidas = {"carne":{"animales":["leon","tigre"]}, "frutas":{"animales":["mono","elefante"]}}
# Añade al diccionario de comidas 4 alimentos mas usando update(clave=valor)
# Existe en la lista de comidas la comida 'carne'?
# Elimina la comida 'frutas' del diccionario de comidas

comidas = {"carne": {"animales": ["leon", "tigre"]}, "frutas": {"animales": ["mono", "elefante"]}}
comidas.update({"pescado": {"animales": ["pingüino", "oso"]}, "insectos": {"animales": ["loro", "lagartija"]}, "vegetales": {"animales": ["jirafa", "cebra"]}, "hierba": {"animales": ["conejo", "ciervo"]}})
existe_carne = 'carne' in comidas
del comidas['frutas']
print("¿Existe la comida 'carne' en la lista de comidas?", existe_carne)
print("Diccionario de comidas actualizado:", comidas)


