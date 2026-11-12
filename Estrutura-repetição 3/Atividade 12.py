contador = 1
contadorMutiplo3 = 0
somaPares = 0

while contador <= 50 :
    numero = int(input("Insira um número: "))
    contador += 1

    if numero % 3 == 0:
        contadorMutiplo3 += 1
    
    if numero % 2 == 0:
        somaPares += numero

print("A quantidade de múltiplos de três é: ", contadorMutiplo3)
print("A soma de todos os números pares é de: ", somaPares)