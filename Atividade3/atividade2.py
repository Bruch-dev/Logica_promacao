totalH = 0
totalM = 0

for i in range(1,57):
    nom = str(input("Qual é o nome da pessoa?: "))
    sex = str(input("Qual é o sexo da pessoa(M- homem e F- mulher)?: "))

    if sex == "M" or sex == "m":
        totalH += 1

    elif sex == "F" or sex == "f":
        totalM += 1

    else:
        print("Sexo não identificado.")

print("O total de homem(s) é de", totalH)
print("O total de mulher(s) é de", totalM)