salario = 0 
somaSalario = 0
maiorSalario = 0
qtdMaior100 = 0 
qtdpessoas = 0
filhos = 0
somaFilhos = 0

while salario >= 0:
    salario = float(input("Digite seu salário: "))
    if salario < 0:
        break
    filhos = int(input("Digite a quantidade de filhos: "))
    qtdpessoas += 1
    somaSalario += salario 
    somaFilhos += filhos

    if maiorSalario < salario:
       maiorSalario = salario
    if salario < 100:
        qtdmenor100 += 1

print("média dos salários:", (somaSalario / qtdpessoas))
print("média dos filhos", (somaFilhos / qtdPessoas))
print("maior salário:", maiorSalario)
print("percentual das pessoas com até 100:", ((qtdMenor100*100)/qtdPessoas)) 