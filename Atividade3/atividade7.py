div = float(input("Qual é o valor da sua divida?: "))
jur = int(input("Em quantas parcelas você deseja pagar a divida(1,3,6,9,12)?: "))

if jur == 1:
    valJ = div * 0
    valP = div * 1
    valTj = div * 1

elif jur == 3:
    valJ = div * 0.1
    valP = (div * 1.1) / 3
    valTj = div * 1.1

elif jur == 6:
    valJ = div * 0.15
    valP = (div * 1.15) / 6
    valTj = div * 1.15

elif jur == 9:
    valJ = div * 0.2
    valP = (div * 1.2) / 9
    valTj = div * 1.2

elif jur == 12:
    valJ = div * 0.25
    valP = (div * 1.25) / 12
    valTj = div * 1.25

else:
    print("Não temos essa opção de parcela.")


print("O valor total da sua divida com juros é de", valTj, "reais.")
print("O valor do juros é de", valJ , "reais.")
print("A quantidade de parecela(s) é de", jur , "parecela(s).")
print("O valor da(s) parcela é de", valP , "reais.")