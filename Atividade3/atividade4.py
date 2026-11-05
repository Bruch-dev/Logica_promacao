valorC = 0

for i in range (1, 16):
    
    com = int(input("Digite o valor da compra: "))
    valorC = valorC + com

pag = int(input("Você deseja pagar como(1- à vista, 2- a prazo)?: "))

if pag == 1:
    valorA = valorC - (valorC * 0.1)

    print("O valor total da sua compra é de", valorC,"reais.")
    print("O valor da sua compra com o desconto à vista é de", valorA,"reias.")

elif pag == 2:
    valorP = valorC * 1.10

    print("O valor total da sua compra é de", valorC,"reais.")
    print("O valor da sua compra total da sua compra com prestação é de", valorP,"reias.")
    print("O valor da primeira prestação é de", valorP / 3,"reais.")

else:
    print("Forma de pagamento não identificada.")