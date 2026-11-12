codigoCidade = 0; numeroVeiculos = 0; numeroAcidentes = 0
maiorAcidente = 0
cidadeMaior = 0
cidadeMenor = 0
somaTodasCidades = 0
somaSCVeiculos = 0
somaSCAcidentes = 0
qtdSC = 0
somaRSVeiculos = 0
somaRSAcidentes = 0
qtdRS = 0
somaPRVeiculos = 0
somaPRAcidentes = 0
qtdPR = 0
menorAcidente = float("inf")
for contador in range (1,12):
    codigoCidade = int(input("Digite o código da cidade: "))
    numeroVeiculos = int(input("Digite o número de veículos: "))
    numeroAcidentes = int(input("Digite o número de acidentes: "))

    if numeroAcidentes > maiorAcidente:
        maiorAcidente = numeroAcidentes
        cidadeMaior = codigoCidade
    if numeroAcidentes < menorAcidente:
        menorAcidente = numeroAcidentes
        cidadeMenor = codigoCidade

    somaTodasCidades += numeroVeiculos

    if codigoCidade >= 11 and codigoCidade <= 14:
        somaSC += numeroVeiculos
        qtdSC += 1

    print("A média de veículos no Brasil é: ", (somaTodasCidades / 12))
    print("A média de veículos em SC é: ", (somaSCVeiculos / qtdSC))
    print ("A média de acidentes em SC é: ", (somaSCAcidentes / qtdSC))

    if codigoCidade >= 21 and codigoCidade <= 24:
        somaRS += numeroVeiculos
        qtdRS += 1

    print("A média de veículos no Brasil é: ", (somaTodasCidades / 12))
    print("A média de veículos no RS é: ", (somaRSVeiculos / qtdRS))
    print ("A média de acidentes no RS é: ", (somaRSAcidentes / qtdRS))

    if codigoCidade >= 31 and codigoCidade <= 34:
        somaPR += numeroVeiculos
        qtdPR += 1

    print("A média de veículos no Brasil é: ", (somaTodasCidades / 12))
    print("A média de veículos no PR é: ", (somaPRVeiculos / qtdPR))
    print ("A média de acidentes no PR é: ", (somaPRAcidentes / qtdPR))
