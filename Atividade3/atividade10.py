clie = 0
idaEx = 0
pesEx = 0
clieP = 0
clieB = 0

for i in range (1, 11):

    ida = int(input("Olá, qual é a sua idade para validar a sua avaliação: "))
    clie += 1

    ava = int(input("Qual é a nota que você da pra loja(péssimo = 1, regular = 2, bom = 3, excelente = 4): "))

    if ava == 1:
        clieP += 1

    elif ava == 2:
        clieB += 1
    
    elif ava == 4:
        idaEx = idaEx + ida
        pesEx += 1

print("A média das idades que colocou exelente é de", idaEx / pesEx, "anos.")
print("O total de clientes que responderam péssimo é de", clieP, "pessoas.")
print("A porcentagem de clientes que responderam bom é de",(clieB / clie) * 100)    