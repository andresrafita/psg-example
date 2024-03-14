# 2. De la siguiente lista [1,2,3,4,5,6,7,8,9,10] obtener una sublista inversa con los elementos multiplos de 3

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sublista = [x for x in lista[::-1] if x % 3 == 0]

print(sublista)
