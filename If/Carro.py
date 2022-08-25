n1 = int(input('Quantos anos tem seu carro? '))

if n1<5:
    print('Carro novo')
else:
    print('Carro velho')

#ou

print('Carro novo' if n1<5 else 'Carro velho')
