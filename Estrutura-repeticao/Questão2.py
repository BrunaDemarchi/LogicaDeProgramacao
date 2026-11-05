numTabuada = int(input("Digite que tabuada você quer: "))
limite = int(input("Digite até que número deseja que a tabuada multipique: "))


for tabuada in range (0, limite + 1):
   multiplicacao = numTabuada * tabuada
   print(multiplicacao)