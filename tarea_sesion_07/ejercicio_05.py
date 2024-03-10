# 5. Escribir un programa que revisa una cadena y retornar verdadero o falso si es palindrome la frase o palabra ejemplo "Anita lava la Tina" es verdad

frase = "Anita lava la Tina"
frase_sin_espacios = frase.replace(" ", "").lower()
es_palindrome = frase_sin_espacios == frase_sin_espacios[::-1]
print(es_palindrome)

