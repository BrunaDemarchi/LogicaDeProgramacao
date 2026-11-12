contador = 1
contadorExcelente = 0

somaIdadeExcelente = 0
somaPessoasPessimo = 0
somaPessoasBom = 0

while contador <= 8:
    
    idade = int(input("Insira sua idade: "))
    opiniao = int(input("Insira sua opinião sobre o filme: \n4 - Excelente \n3 - Bom \n2 - Regular \n1 - Péssimo \nDigite aqui: "))

    if opiniao == 4:
        somaIdadeExcelente += idade
        contadorExcelente += 1
        contador += 1

    elif opiniao == 3:
        somaPessoasBom += 1
        contador += 1

    elif opiniao == 1:
        somaPessoasPessimo += 1
        contador += 1
    
    elif opiniao == 2:
        contador += 1

    else:
        print("Código Inválido")

mediaIdadeExcelente = somaIdadeExcelente / contadorExcelente
porcentagemBom = (somaPessoasBom / (contador - 1)) * 100

print("A média das idades das pessoas que respondeu Excelente é de: ", mediaIdadeExcelente, " anos")
print("A quantidade de pessoas que respondeu Péssimo é de: ", somaPessoasPessimo, " pessoas")
print("A percentagem de pessoas que respondeu bom é de: ", porcentagemBom, " porcento")