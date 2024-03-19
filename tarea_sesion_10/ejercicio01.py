# 1. Anita y Pepito llevan saliendo juntos por 4 semanas, cada vez que salen van a comer a una plaza de comidas. Ambos quieren saber que tan compatibles son viendo cuantos platos de comida tienen en comun. A continuacion tienes los platos de comida que ambos han ido pidiendo a lo largo de sus citas:
# Anita: Sushi, Pizza, Tacos, Hamburguesa, Pasta, Alitas
# Pepito: Pizza, Tacos, Ensalada, Pasta, Helado, Milanesa
# Si la cantidad de platos de comida que tienen en comun mayor a 50% entonces ambos seguiran saliendo.

Anita = {'Sushi', 'Pizza', 'Tacos', 'Hamburguesa', 'Pasta', 'Alitas'}
Pepito = {'Pizza', 'Tacos', 'Ensalada', 'Pasta', 'Helado', 'Milanesa'}

platos_en_comun = Anita & Pepito

porcentaje_de_platos_en_comun = (len(platos_en_comun) / len(Anita.union(Pepito))) * 100

if porcentaje_de_platos_en_comun > 50:
    print("Anita y Pepito son compatibles con un {:.2f} porcentaje de platos en común".format(porcentaje_de_platos_en_comun))
    print("Sigamos saliendo :)")
else:
    print("Anita y Pepito no son compatibles con un {:.2f} porcentaje de platos en común".format(porcentaje_de_platos_en_comun))
    print("Ya no sigamos saliendo :(")




