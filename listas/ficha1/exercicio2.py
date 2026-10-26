import random

notas = []

i = 0

while i < 15:
    notas = notas + [random.randint(0,20)]
    i = i + 1

print(notas)

AlunosAprovados = 0
AlunosReprovados = 0
AlunosMais16 = 0

for n in notas:
    if n >= 10:
        AlunosAprovados = AlunosAprovados + 1
    else: 
        AlunosReprovados = AlunosReprovados + 1

    for n in notas:
        if n >= 16:
            AlunosMais16 = AlunosMais16 + 1

print(AlunosAprovados)

print(AlunosReprovados)

print(AlunosMais16)

print(f"Maior Nota: " , max(notas))

print(f"Menor Nota: " , min(notas))

print(round(sum(notas) / len(notas), 2))

print(round((AlunosAprovados / len(notas)) * 100, 2))

