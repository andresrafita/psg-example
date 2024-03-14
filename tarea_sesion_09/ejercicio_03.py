#  3. Crear una lista de personas con 10 nombres de personas:
# Obtener una sublista de 2 a 7 
# Buscar si existe el nombre "Jhon" en la lista original
# Ordenar la sublista alfabeticamente
# Ordenar la lista original alfabeticamente de forma descendente

lista = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Ivan", "Jhon"]

sublista = lista[1:7]
existe_jhon = "Jhon" in lista
sublista.sort()
lista.sort(reverse=True)

print("Sublista:", sublista)
print("¿Existe 'Jhon'?", existe_jhon)
print("Lista ordenada de forma descendente:", lista)
