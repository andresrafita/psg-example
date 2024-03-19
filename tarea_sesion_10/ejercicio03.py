# Dos mochileros se encuentran en el Salar de Uyuni y se ponen a comparar la cantidad de lugares que han visitado
# Cada uno quiere saber en que parte del mundo ha estado el otro que el no haya visitado

mochilero_a = {"Paris", "Londres", "Nueva York", "Tokio", "Peru", "Chile", "Colombia", "Bolivia"}
mochilero_b = {"Londres", "Roma", "Nueva York", "Sidney", "Argentina", "Brasil", "Panama", "Bolivia"}

lugares_no_visitados_a = mochilero_b - mochilero_a
lugares_no_visitados_b = mochilero_a - mochilero_b

print("Lugares que el mochilero 'a' no ha visitado:")
print(lugares_no_visitados_a)

print("\nLugares que el mochilero 'b' no ha visitado:")
print(lugares_no_visitados_b)



