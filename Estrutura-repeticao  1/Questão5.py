num = int(input("Digite 0 se quiser parar e qualquer outro número para continuar: "))
qtdValores = 0
somaPar = 0
mediaPar = 0


while num != 0:
   if num % 2 == 0:
       qtdValores += 1
       somaPar += num
       mediaPar = somaPar / qtdValores
   num = int(input("Digite 0 se quiser parar e qualquer outro número para continuar: "))


print("A média dos valores pares é: ", mediaPar)
