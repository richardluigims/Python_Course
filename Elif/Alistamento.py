from datetime import date

print('Vamos conferir a possibilidade de seu alistamento militar!')

atual = date.today().year
nasc = int(input('Em que ano você nasceu? '))
idade = atual - nasc

if idade < 18:
    print(f'Falta(m) {18-idade} ano(s) para você poder se alistar.')
elif idade > 18:
    print(f'Você já deveria ter se alistado há {idade - 18} ano(s)!!')
else:
    print(f'Você deve se alistar esse ano.')
