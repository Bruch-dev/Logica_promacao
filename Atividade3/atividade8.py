salaAdm = 0
salaOpe = 0
opeF = 0
admF = 0

for i in range (1, 21):

    fun = int(input("Em qual setor você trabalha(1- setor administrativo, 2- setor operacional)?: "))
    
    if fun == 1:
        admF += 1    

        salarA = float(input("Qual é seu salário?: "))
        salaAdm = salaAdm + salarA
        

    elif fun == 2:
        opeF += 1
        
        salarO = float(input("Qual é o seu salário?: "))
        salaOpe = salarO + salaOpe

    else:
        print("Esse setor não está disponível.")

print("A média salárial do setor administrativo é de",salaAdm / admF, "reais.")
print("A média salárial dp setor operacional é de",salaOpe / opeF, "reias.")
print("O total que a empresa gasta com salário é de",salaAdm + salaOpe, "reais.")
print("No setor administrativo á",opeF, "colaboradores.")
print("No setor operacional á",admF, "colaboradores.")    