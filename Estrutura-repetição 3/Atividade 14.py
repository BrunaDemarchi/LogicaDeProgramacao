temperatura = float(input("Insira a temperatura: "))
contador1 = 0
contador2 = 0
contador3 = 0

while temperatura != 999:

    if temperatura < -50 or temperatura > 150:
        pass

    elif temperatura >= 20 and temperatura <= 80:
        contador1 += 1

    elif temperatura % 5 == 0:
        contador2 += 1

    elif temperatura % 10 != 0:
        contador3 += 1

    temperatura = float(input("Insira a temperatura ou 999 para parar: "))

print("Temperaturas entre 20 e 80: ", contador1)
print("Temperaturas múltiplas de 5: ", contador2)
print("Temperaturas que não são divisíveis por 10: ", contador3)