from random import choice, shuffle

print('Vamor sortear quatro alunos!\n')
aluno1 = input('Digite o nome do aluno 1: ')
aluno2 = input('Digite o nome do aluno 2: ')
aluno3 = input('Digite o nome do aluno 3: ')
aluno4 = input('Digite o nome do aluno 4: ')
lista = [aluno1, aluno2, aluno3, aluno4]

print(f'O aluno sorteado foi {choice(lista)}!')

shuffle(lista)

print(f'A ordem da apresentação será {lista}.')
