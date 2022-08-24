n1 = float(input('Quanto custa seu produto? '))
desconto = n1 - ((n1 * 5)/100)

print(f'Na promoção seu produto custa R${desconto:.2f}.')

n2 = float(input('Digite seu salário: '))
Aumento = n2 + ((n2 * 15)/100)

print(f'Seu novo salário é R${Aumento:.2f}.')
