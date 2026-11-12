processamento = int(input("Insira o processamento das estações: "))
metaDiaria = int(input("Insira a meta diária: "))

producaoTotal = 0
ciclo = 0
pecasNaoProcessadas = 0
pecasProcessadas = 0

contador1 = 0
contador2 = 0
contador3 = 0
contador4 = 0
contador5 = 0

estacaoFalhou = 0

while metaDiaria > producaoTotal and estacaoFalhou == 0:

    estacao = int(input("Insira qual estação (1 a 5): "))
    pecas = int(input("Insira a quantidade de peças: "))

    ciclo += 1

    if pecas > processamento * 90 / 100:

        if estacao == 1:
            contador1 += 1
        else:
            contador1 = 0

        if estacao == 2:
            contador2 += 1
        else:
            contador2 = 0

        if estacao == 3:
            contador3 += 1
        else:
            contador3 = 0

        if estacao == 4:
            contador4 += 1
        else:
            contador4 = 0

        if estacao == 5:
            contador5 += 1
        else:
            contador5 = 0

    else:
        if estacao == 1:
            contador1 = 0
        elif estacao == 2:
            contador2 = 0
        elif estacao == 3:
            contador3 = 0
        elif estacao == 4:
            contador4 = 0
        elif estacao == 5:
            contador5 = 0

    if contador1 >= 5:
        estacaoFalhou = 1
        print("A estação 1 falhou!")

    elif contador2 >= 5:
        estacaoFalhou = 2
        print("A estação 2 falhou!")

    elif contador3 >= 5:
        estacaoFalhou = 3
        print("A estação 3 falhou!")

    elif contador4 >= 5:
        estacaoFalhou = 4
        print("A estação 4 falhou!")

    elif contador5 >= 5:
        estacaoFalhou = 5
        print("A estação 5 falhou!")

    if estacaoFalhou == 0:

        pecasDisponiveis = pecasNaoProcessadas + pecas

        if pecasDisponiveis > processamento:
            pecasProcessadas = processamento
        else:
            pecasProcessadas = pecasDisponiveis

        pecasNaoProcessadas = pecasDisponiveis - pecasProcessadas

        if estacao == 5:
            producaoTotal += pecasProcessadas

print("Produção total:", producaoTotal)
print("Quantidade de ciclos:", ciclo)

if estacaoFalhou != 0:
    print("Falha estrutural na estação:", estacaoFalhou)
else:
    print("Meta diária atingida!")