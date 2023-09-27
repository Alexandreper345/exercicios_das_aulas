import random

def add_alunos():
    add = input('qual aluno você quer add na lista: ')
    f =  open('alunos.txt', 'a')
    f.write('\n'+ add)
    inteiro.append(add)
     


def remove_name():
    remov = input('qual aluno você quer remover da lista: ')
    inteiro.remove(str(remov))



with open('alunos.txt' , 'r') as alun:
    txt = alun.read()
    inteiro = list(map(str,txt.split('\n')))
    print(random.choice(inteiro))

add_alunos()
remove_name()

alun_write = open("alunos.txt", "w")
alun_write.write("")

alun_append = open("alunos.txt", "a")
for TXT in inteiro:
    alun_append.write(TXT+"\n")

