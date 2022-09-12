n1 = float(input("Digite seu salário: "))

if n1 > 1250:
    print(f'Seu salário agora é R$ {n1+n1*0.1:.2f}')
else:
    print(f'Seu salário agora é R$ {n1+n1*0.15:.2f}')
