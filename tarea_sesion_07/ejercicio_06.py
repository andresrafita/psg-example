# 6. Agregar 5 ejemplos con otras funciones no vistas en la sesión. Utilizar la documentación "Metodos de cadenas"

#ejemplo1
cadena = "Hola mundo"
resultado = cadena.endswith("mundo")
print(resultado)

#ejemplo2
texto_con_tabs = "Columna1\tColumna2\tColumna3"
print("Texto original:")
print(texto_con_tabs)
texto_expandido = texto_con_tabs.expandtabs(4)
print("\nTexto con tabulaciones expandidas:")
print(texto_expandido)

#ejemplo3
cadena = "Pre-Ejemplo"
cadena_sin_prefijo = cadena.removeprefix("Pre-")
print(cadena_sin_prefijo) 

#ejemplo4
cadena = "Ejemplo-Post"
cadena_sin_sufijo = cadena.removesuffix("-Post")
print(cadena_sin_sufijo) 

#ejemplo5
cadena = "Hola mundo"
resultado = cadena.startswith("Hola")
print(resultado) 




