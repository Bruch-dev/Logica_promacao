#14- 
#Entrada contínua de temperaturas.
#Regras:
#Ignorar valores < -50 ou > 150
#Encerrar com 999
#Contar temperaturas:
#Entre 20 e 80
#Múltiplas de 5
#Que não sejam divisíveis por 10
#Exibir:
#Quantidade válida
#Maior temperatura válida
#Percentual válido sobre total digitado


tempV = 0 
maioT = 0
tempN = 0

while True:
    tem = float(input("Digite uma temperatura(encerrar com 999): "))
    tempN += 1

    if tem == 999:
        break
    
    if tem > maioT:
        maioT = tem

    if tem >= -50 and tem <= 150:
        tempV += 1

    if tem % 5 == 0 and tem % 10 != 0:
        tempV += 1 

print("A(s) temperatura(s) valida(s) no total é(são)", tempV)
print("A maior temperatura registrada é de", maioT, "graus celcius.")
print("O percentual de temperaturas validas é de", (tempV / tempN) * 100, "%")