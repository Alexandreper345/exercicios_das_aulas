import random

a1 = str(input("qual o nome do aluno 1: "))
a2 = str(input("qual o nome do aluno 2: "))
a3 = str(input("qual o nome do aluno 3: "))
a4 = str(input("qual o nome do aluno 4: "))
lsta = [a1 ,a2 ,a3 , a4]


sorteio = random.choice(lsta)

print("o aluno que vai apagar o quadro é", sorteio)





