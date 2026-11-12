codigoClassificacao = 1

while codigoClassificacao != 0: 
    codigoClassificacao = int(input("Código de classificação: "))

    if codigoClassificacao == 1:
        print ("Alimento não perecível")
    elif codigoClassificacao >=2 and codigoClassificacao <=4:
        print ("Alimento Perecível")
    elif codigoClassificacao >=5 and codigoClassificacao <= 6:
        print ("Vestuário")
    elif codigoClassificacao == 7:
        print ("Higiene pessoal")
    elif codigoClassificacao >=8 and codigoClassificacao <=16: 
        print ("Limpeza e utensílios domésticos")
    else:
        print ("Código de classificação não identificado")