# Tienes una tienda de abarrotes y tienes dos listas, una con los productos que tienes y otra con los precios:
# Agregar 5 productos nuevos al final de las listas 
# Eliminar el producto con el nombre "leche" de las listas
# Cuando cuesta el producto "pan" y "huevo"
# Cual es el producto mas caro y mas barato

productos = ["leche", "pan", "huevo", "carne", "papa"]
precios = [5, 0.5, 0.5, 20, 15]

productos.extend(["agua", "arroz", "aceite", "sal", "azúcar"])
precios.extend([1, 2, 10, 3, 4])

indice_leche = productos.index("leche")
del productos[indice_leche]
del precios[indice_leche]

precio_pan = precios[productos.index("pan")]
precio_huevo = precios[productos.index("huevo")]

producto_mas_caro = productos[precios.index(max(precios))]
producto_mas_barato = productos[precios.index(min(precios))]

print("Productos:", productos)
print("Precios:", precios)
print("Precio del pan:", precio_pan)
print("Precio del huevo:", precio_huevo)
print("Producto más caro:", producto_mas_caro)
print("Producto más barato:", producto_mas_barato)

