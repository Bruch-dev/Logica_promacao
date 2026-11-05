contador = 0

for i in range (1, 6):
    
    num = int(input("Digite algum número: "))
    
    if num >= 10 and num <= 150:
        contador += 1

print("Você digitou", contador,"números entre 10 a 150.") 