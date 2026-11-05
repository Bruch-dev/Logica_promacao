par = 0
mult3 = 0

for i in range (1, 51):

    num = int(input("Digite sua sequência de 50 número inteiros: "))

    if num % 3 == 0:
        mult3 += 1

    if num % 2 == 0:
        par += 1

print("Na sua sequência á", mult3, "número(s) multiplo de 3.")
print("Na sua sequência á", par, "número(s) par(es).")