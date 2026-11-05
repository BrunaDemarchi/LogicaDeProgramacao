num1 = 0
num2 = int(input("Digite um número inteiro e positivo: "))


for numero in range(num2, num1 - 1, -1):
   if numero % 2 == 0:
       print(numero)