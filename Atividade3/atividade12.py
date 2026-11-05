ano = 0

paisA = float(input("Qual é a população do país A?: "))
paisB = float(input("Qual é a população do país B?: "))

if paisA > paisB:
    print("País A não precisou de nenhum ano para ultrapassar o país B.")
else:
    while paisA <= paisB:
        ano += 1  
        
        paisA *= 1.03
        paisB *= 1.015

        if ano % 5 == 0:
            paisA *= 0.93
            paisB *= 0.93

    print("O país A ultrapassou o país B em", ano, "anos.")