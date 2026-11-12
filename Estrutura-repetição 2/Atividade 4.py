jogador1 = 0
jogador2 = 0
diferencaPontos = 0

while jogador1 < 21 and jogador2 < 21 or diferencaPontos >= 2:
    vitoria = int(input("Digite quem ganhou: "))

    if vitoria == 1:
        jogador1 += 1
    elif vitoria == 2:
        jogador2 += 1

if jogador1 >= 21 :
    print ("Jogador 1 ganhou")
else :
    print ("Jogador 2 ganhou")