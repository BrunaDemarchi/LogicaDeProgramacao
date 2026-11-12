num = 1
totalP = 0
totalN = 0
nN = ""
nP = ""

while num != 0: 
    num = int(input("Digite um número: "))

    if num%2 == 0 and num != 0:
        nP += str(num) + " "

    elif num != 0:
        nN += str(num) + " "

    if num > 0:
        totalP += num

    elif num < 0:
        totalN += num

print ("A soma dos números positivos é: ", totalP)
print ("A soma dos números negativos é: ", totalN)
print ("Soma total: ", totalN + totalP)
print (nP)
print (nN)
