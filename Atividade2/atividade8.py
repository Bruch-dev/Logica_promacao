while True:
    carV = int(input("Digite o valor do carro: "))
    
    valTv = carV * 0.80

    pag = int(input("Pretende pagar como(1- a vista e 2- parcelado)?: "))

    if pag == 1:
        valT = valTv
        met = 1
        par = valT

    elif pag == 2:
        met = int(input("Quantas parecelas deseja fazer(6, 12, 18, 24, 30, 36, 42, 48, 54 e 60)?: "))

        if met == 6:
            valT = carV * 1.03
        elif met == 12:
            valT = carV * 1.06
        elif met == 18:
            valT = carV * 1.09
        elif met == 24:
            valT = carV * 1.12
        elif met == 30:
            valT = carV * 1.15
        elif met == 36:
            valT = carV * 1.18
        elif met == 42:
            valT = carV * 1.21
        elif met == 48:
            valT = carV * 1.24
        elif met == 54:
            valT = carV * 1.27
        elif met == 60:
            valT = carV * 1.30
        else:
            print("parcelas n identificada.")
            continue

        par = valT / met

    else:
        print("Opção inválida.")
        continue

    print("O preço final do carro é de", valT, "reais")
    print("A quantidade de parcelas escolhidas foi de", met)
    print("O valor das parcelas é de", par, "reais")
    print("O valor a vista do carro é de", valTv, "reais")
    break