contador = 1
contador2 = 0

while contador <= 80:
    num = int(input("Escreva um número: "))
    contador += 1
    if num >= 10 and num <= 150:
        contador2 += 1

print("A quantidade de números que está entre 10 (inclusive) e 150 (inclusive) é de: ", contador2)