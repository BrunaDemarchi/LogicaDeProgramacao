contador = 1
contadorMasculino = 0
contadorFeminino = 0

while contador <= 56:
    nome = input("Insira o nome: ")
    sexo = input("Digite o sexo: ")

    if sexo.lower() == "masculino" or sexo.lower() == "homem":
        contadorMasculino += 1
        contador += 1

    elif sexo.lower() == "feminino" or sexo.lower() == "mulher":
        contadorFeminino += 1
        contador += 1

    else:
        print("Sexo não válido")

print("A quantidade de Homens é de: ", contadorMasculino)
print("A quantidade de Mulheres é de: ", contadorFeminino)