from math import hypot

n1 = float(input('Digite o valor do cateto oposto: '))
n2 = float(input('Digite o valor do cateto adjacente: '))
hip = hypot(n1,n2)

print(f'O valor da hipotenusa do seu triângulo é {hip:.2f}')
