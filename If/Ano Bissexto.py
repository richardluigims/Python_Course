from datetime import date

n1 = int(input('Digite um ano qualquer: '))

if n1 == 0:
    n1 = date.today().year

print(f'O ano {n1} é bissexto!' if n1%4 == 0 and n1%100 != 0 or n1%400 == 0 else f'O ano {n1} não é bissexto')
