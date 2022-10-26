print('Vamos converter um número para binário, octal ou hexadecimal! \nPara converter, siga a seguinte relação: 1 - binário. 2 - octal. 3 - hexadecimal\n')

n1 = int(input('Digite um número qualquer: '))
n2 = int(input('Para qual base deseja converter? '))

while n2 != 1 and n2 != 2 and n2 != 3:
    n2 = int(input('Valor inválido! Tente novamente: '))

if n2 == 1:
    print(f'O valor {n1} convertido em binário é {bin(n1)[2:]}')
elif n2 == 2:
    print(f'O valor {n1} convertido em octal é {oct(n1)[2:]}')
elif n2 == 3:
    print(f'O valor {n1} convertido em hexadecimal é {hex(n1)[2:]}')
