preco = float(input("Digite o valor do carro: "))
qtdParcelas = int(input("Digite a quatnidade de parcelas: (6, 12, 18, 24, 30, 36, 42, 48, 54 ou 60) "))
avista = preco * 0.80

precoFinal = preco + (preco * 0.03)

match qtdParcelas: 
    case 6 :
        precoFinal = preco + (preco * 0.03)
        print ("O preço final é: ", precoFinal)
    case 12 :
        precoFinal = preco + (preco * 0.06)
        print ("O preço final é: ", precoFinal)
    case 18 :
        precoFinal = preco + (preco * 0.09)
        print ("O preço final é: ", precoFinal)
    case 24 :
        precoFinal = preco + (preco * 0.12)
        print ("O preço final é: ", precoFinal)
    case 30 :
        precoFinal = preco + (preco * 0.15)
        print ("O preço final é: ", precoFinal)
    case 36 :
        precoFinal = preco + (preco * 0.18)
        print ("O preço final é: ", precoFinal)
    case 42 :
        precoFinal = preco + (preco * 0.21)
        print ("O preço final é: ", precoFinal)
    case 48 :
        precoFinal = preco + (preco * 0.24)
        print ("O preço final é: ", precoFinal)
    case 54 :
        precoFinal = preco + (preco * 0.27)
        print ("O preço final é: ", precoFinal)
    case 60 :
        precoFinal = preco + (preco * 0.30)
        print ("O preço final é: ", precoFinal)
    case _:
        print ("Opção inválida")