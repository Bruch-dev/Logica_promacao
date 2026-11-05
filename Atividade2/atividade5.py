contador = 0
paisA = 90
paisB = 140

while paisB >= paisA:
    contador += 1
    paisA *= 1.035  
    paisB *= 1.01   

print("País A passou o país B depois de", contador, "anos.")