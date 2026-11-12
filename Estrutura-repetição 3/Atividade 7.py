contador = int(input("Insira: \n1 - Se quiser continuar o pedido \nQualquer outro número - Para Finalizar o pedido \nDigite aqui: "))
cachorroQuente = 1.20
bauruSimples = 1.30
bauruComOvo = 1.50
hamburguer = 1.20
cheeseburguer = 1.30
refrigerante = 1.00

valorCachorroQuente = 0
valorBauruSimples = 0
valorBauruComOvo = 0
valorHamburguer = 0
valorCheeseburguer = 0
valorRefrigerante = 0

valorTotal = 0

while contador == 1:

    codigo = int(input("Insira o código do produto: "))
    quantidade = int(input("Insira a quantidade: "))

    if codigo == 100:
        valorCachorroQuente += cachorroQuente * quantidade
        valorTotal += valorCachorroQuente
    
    elif codigo == 101:
        valorBauruSimples += bauruSimples * quantidade
        valorTotal += valorBauruSimples

    elif codigo == 102:
        valorBauruComOvo += bauruComOvo * quantidade
        valorTotal += valorBauruComOvo

    elif codigo == 103:
        valorHamburguer += hamburguer * quantidade
        valorTotal += valorHamburguer
    
    elif codigo == 104:
        valorCheeseburguer += cheeseburguer * quantidade
        valorTotal += valorCheeseburguer

    elif codigo == 105:
        valorRefrigerante += refrigerante * quantidade
        valorTotal += valorRefrigerante
    
    contador = int(input("Insira: \n1 - Se quiser continuar o pedido \nQualquer outro número - Para Finalizar o pedido \nDigite aqui: "))

print("O valor gasto em cachorro-quente é de: ", valorCachorroQuente)
print("O valor gasto em Bauru Simples é de: ", valorBauruSimples)
print("O valor gasto em Bauru com Ovo é de: ", valorBauruComOvo)
print("O valor gasto em Hambúrguer é de: ", valorHamburguer)
print("O valor gasto em Cheeseburguer é de: ", valorCheeseburguer)
print("O valor gasto em Refrigerante é de: ", valorRefrigerante)
print("O valor total gasto é de: ", valorTotal)