alun = 0
notaT = 0
nota7 = 0

for i in range (1, 36):

    nome = str(input("Qual é o nome do aluno?: "))   
    alun += 1

    nota = float(input("Qual é a nota do aluno?: "))
    notaT = notaT + nota

    if nota > 7:
        nota7 += 1

print("A média geral da turma é de", notaT / alun, "pontos")
print("A quantidade de aluno que tiraram nota acima de 7 é de", nota7, "aluno(s).")