nome = str(input("Digite seu nome: "))
valorCompras = float(input("Digite o valor das suas compras no ano passado: "))
clientes = 0

if valorCompras < 500000:
    bonus = valorCompras - (valorCompras * 0.10)
    valorCompras - (valorCompras * 0.10)
    print ("O bônus é de: ", bonus)

else:
    bonus = valorCompras - (valorCompras * 0.15)
    valorCompras - (valorCompras * 0.15)
    print ("O bônus é de: ", bonus) 