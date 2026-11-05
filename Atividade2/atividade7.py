# Dicionário para armazenar o total de pessoas em cada canal válido
audiencia = {4: 0, 5: 0, 7: 0, 12: 0}
# Variáveis para acumular o total de pessoas de cada canal
canal_4 = 0
canal_5 = 0
canal_7 = 0
canal_12 = 0
total_geral_pessoas = 0

print("--- Pesquisa de Audiência de TV ---")
print("Canais válidos: 4, 5, 7, 12. Digite 0 para encerrar.")

while True:
    canal = int(input("\nDigite o número do canal: "))
    
    if canal == 0:
        break
        
    if canal != 4 and canal != 5 and canal != 7 and canal != 12:
        print("Canal inválido! Escolha entre 4, 5, 7, 12 ou digite 0 para sair.")
        continue  
        
    pessoas = int(input("Digite o número de pessoas assistindo: "))
    
    if pessoas < 0:
        print("Número de pessoas inválido. Tente novamente.")
        continue

    # Somando no canal correspondente
    if canal == 4:
        canal_4 = canal_4 + pessoas
    elif canal == 5:
        canal_5 = canal_5 + pessoas
    elif canal == 7:
        canal_7 = canal_7 + pessoas
    elif canal == 12:
        canal_12 = canal_12 + pessoas
        
    total_geral_pessoas = total_geral_pessoas + pessoas

print("\n=== RESULTADO DA PESQUISA ===")
print("Total de telespectadores entrevistados:", total_geral_pessoas)

if total_geral_pessoas > 0:
    # Calculando as porcentagens
    porcentagem_4 = (canal_4 / total_geral_pessoas) * 100
    porcentagem_5 = (canal_5 / total_geral_pessoas) * 100
    porcentagem_7 = (canal_7 / total_geral_pessoas) * 100
    porcentagem_12 = (canal_12 / total_geral_pessoas) * 100

    # Mostrando os resultados com arredondamento simples
    print("Canal 4:", round(porcentagem_4, 2), "% de audiência (", canal_4, "pessoas )")
    print("Canal 5:", round(porcentagem_5, 2), "% de audiência (", canal_5, "pessoas )")
    print("Canal 7:", round(porcentagem_7, 2), "% de audiência (", canal_7, "pessoas )")
    print("Canal 12:", round(porcentagem_12, 2), "% de audiência (", canal_12, "pessoas )")
else:
    print("Nenhum dado de audiência foi registrado.")
