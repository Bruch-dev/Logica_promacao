codN = 0
codA = 0
codV = 0
codH = 0
codL = 0

while True:
    print("\nDigite o código do produto (0 para encerrar)")
    print("1 - Alimento não-perecível")
    print("2 a 4 - Alimento perecível") 
    print("5 e 6 - Vestuário") 
    print("7 - Higiene pessoal")
    print("8 a 15 - Limpeza e utensílios domésticos")
    cod = int(input("Qual você deseja?: "))

    if cod == 0:
        break

    if cod == 1:
        codN += 1
    elif 2 <= cod <= 4:
        codA += 1
    elif 5 <= cod <= 6:
        codV += 1
    elif cod == 7:
        codH += 1
    elif 8 <= cod <= 15:
        codL += 1
    else:
        print("Código inválido! Tente novamente.")

print("\n--- RESUMO DA CLASSIFICAÇÃO ---")
print("Você classificou", codN, "alimento(s) não perecível(is).")
print("Você classificou", codA, "alimento(s) perecível(is).")
print("Você classificou", codV, "vestuário(s).")
print("Você classificou", codH, "item(ns) de higiene pessoal.")
print("Você classificou", codL, "item(ns) de limpeza e utensílios domésticos.")