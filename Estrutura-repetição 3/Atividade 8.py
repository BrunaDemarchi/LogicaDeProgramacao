divida = float(input("Insira o valor da dívida: "))

parcelas1 = 1
parcelas3 = 3
parcelas6 = 6
parcelas9 = 9
parcelas12 = 12

juros1 = divida * 0 / 100
juros3 = divida * 10 / 100
juros6 = divida * 15 / 100
juros9 = divida * 20 / 100
juros12 = divida * 25 / 100

divida1 = divida + juros1
divida3 = divida + juros3
divida6 = divida + juros6
divida9 = divida + juros9
divida12 = divida + juros12

valorParcela1 = divida / parcelas1 
valorParcela3 = divida / parcelas3 
valorParcela6 = divida / parcelas6
valorParcela9 = divida / parcelas9 
valorParcela12 = divida / parcelas12

matriz = [
    ["Valor da Divida", "Valor dos Juros", "Valor com os Juros", "Qtd de Parcelas", "Valor da Parcela"],
    [divida, juros1, divida1, parcelas1, valorParcela1],
    [divida, juros3, divida3, parcelas3, valorParcela3],
    [divida, juros6, divida6, parcelas6, valorParcela6],
    [divida, juros9, divida9, parcelas9, valorParcela9],
    [divida, juros12, divida12, parcelas12, valorParcela12],
]

for linha in matriz:
    print("".join(str(item).ljust(22) for item in linha))