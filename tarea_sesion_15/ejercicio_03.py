# 3. Simular un cajero automatico que solicite un monto a retirar, si el monto es mayor al saldo lanzar una excepcion personalizada y si el monto es mayor a 1000 lanzar una excepcion generica

saldo = 5000  # Saldo inicial del cajero automático

while True:
    try:
        monto_retiro = float(input("Ingrese el monto a retirar: "))
        if monto_retiro > saldo:
            raise ValueError("Saldo insuficiente para realizar el retiro")
        elif monto_retiro > 1000:
            raise Exception("Se ha excedido el límite máximo de retiro")
        else:
            saldo -= monto_retiro
            print("Retiro exitoso. Saldo restante:", saldo)
            break
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(e)



















