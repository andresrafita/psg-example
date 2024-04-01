# 1. Un estudiante desea saber cual es su promedio de calificaciones en la materia de matematicas, crea una funcion que reciba las calficaciones como lista y devuelva el promedio lasa calificaciones son 20,40,60,51,13

def promedio_calificaciones(calificaciones):
    return sum(calificaciones) / len(calificaciones)

calificaciones = [20, 40, 60, 51, 13]
promedio = promedio_calificaciones(calificaciones)
print("El promedio de las calificaciones es:", promedio)
























