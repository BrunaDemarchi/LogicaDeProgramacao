contador = 1
contadorOtimo = 0

somaIdadeOtimo = 0
somaPessoasRegular = 0
somaPessoasBom = 0

while contador <= 6:
    
    idade = int(input("Insira sua idade: "))
    opiniao = int(input("Insira sua opinião sobre o filme: \n3 - Ótimo \n2 - Bom \n1 - Regular \nDigite aqui: "))

    if opiniao == 3:
        somaIdadeOtimo += idade
        contadorOtimo += 1
        contador += 1

    elif opiniao == 2:
        somaPessoasBom += 1
        contador += 1

    elif opiniao == 1:
        somaPessoasRegular += 1
        contador += 1
    
    else:
        print("Código Inválido")

mediaIdadeOtimo = somaIdadeOtimo / contadorOtimo
porcentagemBom = (somaPessoasBom / (contador - 1)) * 100

print("A média das idades das pessoas que respondeu ótimo é de: ", mediaIdadeOtimo, " anos")
print("A quantidade de pessoas que respondeu regular é de: ", somaPessoasRegular, " pessoas")
print("A percentagem de pessoas que respondeu bom é de: ", porcentagemBom, " porcento")
