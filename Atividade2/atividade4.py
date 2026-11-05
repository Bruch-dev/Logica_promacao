jogador1 = 0
jogador2 = 0

while True:
    print("o jogo está", jogador1, "x", jogador2)    
    pon = int(input("Quem fez o ponto(1 para jogador 1, 2 para jogador 2)?: "))
    
    if pon == 1:
        jogador1 += 1
    else:
        jogador2 += 1

    if jogador1 >= 21 and (jogador1 - jogador2) >= 2:
        print("Jogador 1 venceu por", jogador1, "x", jogador2)
        break 

    elif jogador2 >= 21 and (jogador2 - jogador1) >= 2:
        print("Jogador 2 venceu por", jogador2, "x", jogador1)
        break