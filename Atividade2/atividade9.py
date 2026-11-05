for i in range(150):
    nome = str(input("Qual é seu nome do cliente: "))
    valor = float(input("Quanto você gastou ano passado com a nossa loja: "))

    if valor < 500000:
        bonus = valor * 0.1

    else:
        bonus = valor * 0.15

    print("Parabéns", nome, "Você ganhou um bonûs de", bonus)