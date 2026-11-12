contador = 1
somaSalarioAdministrativo = 0
somaSalarioOperacional = 0
contadorOperacional = 0
contadorAdministrativo = 0

while contador <= 2:

    codigo = int(input("Insira o código do seu setor: \n1 - Setor Administrativo \n2 - Setor Operacional \nDigite aqui: "))
    
    if codigo == 1:
        salario = float(input("Insira o salário: "))
        somaSalarioAdministrativo += salario
        contadorAdministrativo += 1
    
    elif codigo == 2:
        salario = float(input("Insira o salário: "))
        somaSalarioOperacional += salario
        contadorOperacional += 1

    contador += 1

mediaAdministrativo = somaSalarioAdministrativo / contadorAdministrativo
mediaOperacional = somaSalarioOperacional / contadorOperacional
totalSalarios = somaSalarioAdministrativo + somaSalarioOperacional

print("A média salarial do setor administrativo é: ", mediaAdministrativo)
print("A média salarial no setor operacional é: ", mediaOperacional)
print("O total de salários pagos pela empresa é: ", totalSalarios)
print("A quantidade de funcionários no setor administrativo é: ", contadorAdministrativo)
print("A quantidade de funcionários no setor operacional é: ", contadorOperacional)