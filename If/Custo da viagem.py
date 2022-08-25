n1 = float(input('Digite a quantidade de Km rodados: '))

if n1<=200:
    n2 = n1*0.5
    print(f'Valor a ser pago: R${n2:.2f}')
else:
    n2 = (200*0.5)+((n1-200)*0.45)
    print(f'Valor a ser pago: R${n2:.2f}')
