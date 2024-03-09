#Imprimir tabla de verdad
print("Interruptor 1 | Interruptor 2 | Luz 1 | Luz 2 | Puerta se abre")
for interruptor1 in [False, True]:
    for interruptor2 in [False, True]:
        luz1 = interruptor1
        luz2 = interruptor2
        puerta_abierta = (interruptor1 == interruptor2)
        print(f"     {interruptor1}     |     {interruptor2}     |  {luz1}   |  {luz2}   |      {puerta_abierta}")
