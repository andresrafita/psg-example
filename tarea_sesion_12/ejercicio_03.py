# 3. El usuario Jhon Doe esta en una red social, sus amigos son:
# {Alice, Bob, Charlie, David, Eve}
# Jess Doe tiene los siguientes amigos:
# {Alice, Bob, Frank, Grace}
# Tienen Jhon y Jess amigos en comun y ¿Cuales son?

amigos_jhon = {"Alice", "Bob", "Charlie", "David", "Eve"}
amigos_jess = {"Alice", "Bob", "Frank", "Grace"}

amigos_comunes = amigos_jhon.intersection(amigos_jess)

if amigos_comunes:
    print("Jhon y Jess tienen amigos en común:")
    print(amigos_comunes)
else:
    print("Jhon y Jess no tienen amigos en común.")













