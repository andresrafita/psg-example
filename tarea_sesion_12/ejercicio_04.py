# 4. Una tienda ofrece descuentos a sus clientes, si el cliente es mayor de edad y tiene una compra mayor a 1000, se le aplica un descuento del 10%, si es menor de edad y tiene una compra mayor a 500 se le aplica un descuento del 5%, si no cumple ninguna condicion se le aplica un descuento de 2%

def descuento(edad, compra):
    if edad >= 18 and compra > 1000:
        descuento = 0.10
    elif edad < 18 and compra > 500:
        descuento = 0.05
    else:
        descuento = 0.02
    return descuento

# Ejemplo de uso
edad_cliente = 25
monto_compra = 1200
descuento_aplicado = descuento(edad_cliente, monto_compra)
monto_final = monto_compra * (1 - descuento_aplicado)

print(f"El cliente de {edad_cliente} años y una compra de ${monto_compra} recibe un descuento del {descuento_aplicado * 100}%")
print(f"El monto final a pagar es: ${monto_final}")









