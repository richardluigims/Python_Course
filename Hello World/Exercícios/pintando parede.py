print('Vamos pintar sua parede!')
Larg = float(input('Qual a largura da sua parede (em metros)? '))
Alt = float(input('Qual a altura da sua parede (em metros)? '))
Area = Larg * Alt
QntTinta = Area/2.00 #pintamos 2m2 para cada litro de tinta

print(f'Vamos precisar de {QntTinta:.2f} litro(s) de tinta!')
