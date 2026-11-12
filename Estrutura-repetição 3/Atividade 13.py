contador = 0
populacaoA = int(input("Insira a população do país A: "))
populacaoB = int(input("Insira a população do país B: "))

while populacaoA < populacaoB:

    populacaoA += populacaoA * 3 /100
    populacaoB += populacaoB * 1.5 / 100

    if contador % 5 == 0:
        populacaoA -= populacaoA * 7 / 100
        populacaoB -= populacaoB * 7 / 100

    contador += 1

print("O País A leva ", contador, "anos para ultrapassar o País B em população")