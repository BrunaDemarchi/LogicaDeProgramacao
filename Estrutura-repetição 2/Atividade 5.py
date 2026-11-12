populacaoA = 90000000
populacaoB = 140000000
ano = 0

while populacaoA <= populacaoB:
    populacaoA = populacaoA + (populacaoA * 3.5 / 100)
    populacaoB = populacaoB + (populacaoB * 1 / 100)
    ano += 1

print("A quantidade de anos necessários para a população do pais A ser maior que a do pais B é de: ", ano)