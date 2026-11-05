cac = 0
bauS = 0
bauO = 0
ham = 0
che = 0
ref = 0
valT = 0

print("Olá qual será o pedi de hoje? Aqui está o cardapio.")
print("Especificação      Código     Preço")
print("")
print("Cachorro Quente      1        R$ 1,20")
print("Bauru Simples        2        R$ 1,30")
print("Bauru com ovo        3        R$ 1,50")
print("Hambúrguer           4        R$ 1,20")
print("Cheeseburguer        5        R$ 1,30")
print("Refrigerante         6        R$ 1,00")

while True:

    prod = int(input("Qual é o código do lanche (0 para encerrar o pedido)?: "))

    if prod == 1:
        cac += 1
        valT = 1.20 + valT

    elif prod == 2:
        bauS += 1
        valT = 1.30 + valT

    elif prod == 3:
        bauO += 1
        valT = 1.50 + valT

    elif prod == 4:
        ham += 1
        valT = 1.20 + valT

    elif prod == 5:
        che += 1
        valT = 1.30 + valT

    elif prod == 6:
        ref +=1
        valT = 1 + valT

    elif prod == 0:
        break
    
    else:
        print("Nâo temos um lanche com esse còdigo.")

print("\nO seu pedido é de:")
print(cac, "Cachorro(s) quente(s), custanto",cac * 1.20, "reais.")
print(bauS, "Bauru(s) Simples, custando",bauS * 1.30, "reais.")
print(bauO, "Bauru(s) com ovo, custando",bauO * 1.50, "reais.")
print(ham, "Hamburguer(s), custando", ham * 1.20, "reais.")
print(che, "Cheeseburguer(s), custando",che * 1.30, "reais.")
print(ref, "Refrigerante(s), custando", ref * 1, "reais.")
print("O total so seu pedido é de", valT, "reais")