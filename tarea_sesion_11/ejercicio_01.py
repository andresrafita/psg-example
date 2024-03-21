# 1. Registro de un zoologico, utiliza un diccionario para almacenar información de un animal del zoologico, registra información como especie, habitat, dieta, estado de salud, edad, en una lista los responsables de su cuidado

zoologico = {}
def agregar_animal(nombre, especie, habitat, dieta, estado_salud, edad, responsables):
    zoologico[nombre] = {
        'especie': especie,
        'habitat': habitat,
        'dieta': dieta,
        'estado_salud': estado_salud,
        'edad': edad,
        'responsables': responsables
    }
agregar_animal('Leo', 'León', 'Savana', 'Carnívoro', 'Saludable', 5, ['Juan', 'María'])
print(zoologico)








