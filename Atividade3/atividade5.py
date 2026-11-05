idadeM = 0
contadorP = 0
contB = 0
conIda = 0

for i in range(1, 16):

    nota = int(input("Qual é a sua opnião sobre o filme 1- regular, 2- bom, 3- ótimo: "))
    idade = int(input("Qual a sua idade?: "))
 
    if nota == 3:
        idadeM += idade
        conIda += 1

    elif nota == 2:
        contadorP += 1

    elif nota == 1:
        contB += 1

print("A média das idades das pessoas que responderam ótimo foi de:", idadeM / conIda)
print("A percentagem de pessoas que respondeu bom entre todos os espectadores analisados foi de:", (contadorP / 15) * 100)
print("A quantidade de pessoas que respondeu regular foi de:", contB)