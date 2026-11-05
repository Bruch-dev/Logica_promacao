somaN = 0
somaP = 0

impar = []
par = []

print("Digite os números (digite 0 para encerrar):")

while True:
    num = int(input("Digite um número: "))

    if num == 0:
        break

    if num > 0:
        somaP += num

    else:
        num < 0
        somaN += num

    if num % 2 == 0:
        par.append(num)

    else:
        impar.append(num)

somaT = somaP + somaN

print("A soma dos Número negativos é de", somaN)
print("A soma dos Número positivos é de", somaP)
print("A soma dos números digitados é de ", somaT)
print("Você digitou", impar, "números ímpares")
print("Você digitou", par, "números pares")