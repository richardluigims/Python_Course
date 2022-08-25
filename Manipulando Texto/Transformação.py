n1 = 'Curso em Video Python'
n2 = '   Aprenda Python  '

print(n1.replace('Python', 'Android')) #substitui Python por Android
print(n1.upper()) #tudo maiúsculo
print(n1.lower()) #tudo minúsculo
print(n1.capitalize()) #só a primeira letra da frase maiúscula
print(n1.title()) #todas as primeiras letras maiúsculas, analisa posição dos espaços
print(n1.split()) #divide a frase em outra lista verificando os espaços, cada elemento da lista é uma palavra
print('-'.join(n1.split())) #insere o elemento dentro das aspas entre cada um dos elementos da lista


print(n2.strip()) #remove espaços inúteis, mantém os do meio
print(n2.rstrip()) #remove somente espaços da direita
print(n2.lstrip()) #remove somente espaços da esquerda
