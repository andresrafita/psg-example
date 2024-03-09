#3. Convertir a cuantos días, horas, minutos y segundos corresponde la siguiente cantidad de segundos: 288325

total_segundos = 288325
dias = total_segundos // 86400
horas = (total_segundos % 86400) // 3600
minutos = (total_segundos % 3600) // 60
segundos = total_segundos % 60
print(f"{dias} días, {horas} horas, {minutos} minutos y {segundos} segundos.")

