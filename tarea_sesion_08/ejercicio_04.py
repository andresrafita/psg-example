# 4. Las notas de un estudiante durante un semestre son: 
# 34,61,80,20,12,69,32,60,61,51,90,23,15
# Genera una tupla con los resultados y calcula el promedio para saber si aprobo o no el semestre utiliza la funcion sum() y len()

notas = (34, 61, 80, 20, 12, 69, 32, 60, 61, 51, 90, 23, 15)

promedio = sum(notas) / len(notas)

if promedio >= 60:
    print("El estudiante aprobó con un promedio de", promedio)
else:
    print("El estudiante no aprobó con un promedio de", promedio)
