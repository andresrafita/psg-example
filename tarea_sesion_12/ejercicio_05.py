# 5. Un usuario ingresa su nombre y gustos musicales por teclado separados por coma, verifica si el usuario ingresó un nombre válido usando "truthiness", convertir los gustos musicales en una lista y verifica si tiene el gusto "rock" en su lista de gustos musicales:
# Nombre: Jhon Doe
# Gustos musicales: rock, pop, jazz

entrada = input("Ingrese su nombre y gustos musicales separados por coma: ").split(',')
nombre = entrada[0].strip() if entrada else None
gustos_musicales = [gusto.strip() for gusto in entrada[1:]] if len(entrada) > 1 else []

if nombre:
    print("Nombre válido")
    if "rock" in gustos_musicales:
        print("Tiene gusto por el rock")
    else:
        print("No tiene gusto por el rock")
else:
    print("Nombre inválido")
















