# 4. Gestion de habitats en peligro: Crear un diccionario que asocie especies animales en peligro de extincion con informacion sobre sus habitats amenazados, lo que permite priorizar la proteccion de areas criticas para la supervivencia de estas especies
# habitats = {"polo norte":{"especies":{"oso polar","morsa","ballena"}}, "amazonas":{"especies":{"tigre","mono","guacamayo"}}}
# Añade al diccionario de habitats 2 habitats mas usando update()
# Existe en el diccionario de habitats el habitat 'amazonas'?
# Añade al diccionario de amazonas la especie 'anaconda'

habitats_peligro = {
    "polo norte": {"especies": {"oso polar", "morsa", "ballena"}},
    "amazonas": {"especies": {"tigre", "mono", "guacamayo"}}
}

# Añadir dos habitats más al diccionario de habitats
habitats_peligro.update({
    "arrecife de coral": {"especies": {"tortuga marina", "pez payaso"}},
    "selva africana": {"especies": {"elefante", "gorila", "leopardo"}}
})

# Verificar si el habitat 'amazonas' está en el diccionario de habitats
existe_amazonas = 'amazonas' in habitats_peligro

# Añadir la especie 'anaconda' al habitat 'amazonas'
habitats_peligro['amazonas']['especies'].add('anaconda')

# Imprimir resultados
print("Existe el habitat 'amazonas':", existe_amazonas)
print("Diccionario de habitats actualizado:", habitats_peligro)












