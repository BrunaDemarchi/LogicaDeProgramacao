contador = 1
contadorMaior = 0
somaNota = 0

while contador <= 5:
    nome = input("Insira o nome: ")
    nota = float(input("Insira a nota: "))
    somaNota += nota
    contador += 1

    if nota > 7:
        contadorMaior += 1

media = somaNota / contador - 1

print("A média geral da turma é de: ", media)
print("A quantidade de alunos com nota acima de 7 é de: ", contadorMaior)