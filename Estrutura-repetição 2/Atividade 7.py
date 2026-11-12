somaTotal = 0
soma4 = 0
soma5 = 0
soma7 = 0
soma12 = 0
canal4 = 0
canal5 = 0
canal7 = 0
canal12 = 0
canal = 1

while canal != 0:

    canal = int(input("Digite um canal: "))
    qtdPessoas = int(input("Digite quantas pessoas estavam assistindo: "))

    if canal == 4:
        canal4 += 1
        soma4 += qtdPessoas

    elif canal == 5:
        canal5 += 1
        soma5 += qtdPessoas

    elif canal == 7:
        canal7 += 1
        soma7 += qtdPessoas

    elif canal == 12:
        canal12 += 1
        soma12 += qtdPessoas

    somaTotal = somaTotal + qtdPessoas

audiencia4 = (soma4 / somaTotal) * 100
audiencia5 = (soma5 / somaTotal) * 100
audiencia7 = (soma7 / somaTotal) * 100
audiencia12 = (soma12 / somaTotal) * 100

print ("A porcentagem de audiência no canal 4 é: ", audiencia4)
print ("A porcentagem de audiência no canal 5 é: ", audiencia5)
print ("A porcentagem de audiência no canal 7 é: ", audiencia7)
print ("A porcentagem de audiência no canal 12 é: ", audiencia12)