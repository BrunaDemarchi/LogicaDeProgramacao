contador = 1
valorAVista = 0
valorAPrazo = 0

while contador <= 15:

    valor = float(input("Insira o valor da compra: "))
    codigo = int(input("Insira: \n1 - Para Transação à vista \n2 - Para Transação a prazo \nInsira o código da transação: "))

    if codigo == 1:
        valorAVista += valor
        contador += 1

    elif codigo == 2:
        valorAPrazo += valor
        contador += 1

valorTotal = valorAVista + valorAPrazo
valorPrimeiraPrestacao = valorAPrazo / 3

print("O valor total das compras à vista é de: ", valorAVista)
print("O valor total das compras a prazo é de: ", valorAPrazo)
print("O valor total de todas as compras é de: ", valorTotal)
print("O valor da primeira prestação das compras à prazo é de: ", valorPrimeiraPrestacao)