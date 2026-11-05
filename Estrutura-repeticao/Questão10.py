num = int(input("Digite quantas linhas quer que o triângulo tenha: "))


for contador in range(1, num + 1):
   for numero in range(1, contador + 1):
       print(numero, end=" ")
   print()