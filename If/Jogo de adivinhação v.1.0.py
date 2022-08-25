from random import randint

n1 = randint(0,5)
n2 = int(input('Digite um número de 0 a 5: '))

print(n1)
print('Você venceu' if n2==n1 else 'Você perdeu')
