n1 = float(input('Quanto custa seu produto? '))
desc = (n1 * 5)/100

print(f'Na promoção seu produto custa R${n1-desc:.2f}.')

n2 = float(input('Digite seu salário: '))
Aumento = (n2 * 15)/100

print(f'Seu novo salário é R${n2+Aumento:.2f}.')
