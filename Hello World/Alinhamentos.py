print('Oi'*5) # vai printar Oi 5 vezes
#Alinhamentos
nome = input('Qual é o seu nome? ')
print(f'Prazer em te conhecer {nome:20}!') # print: Richard           !
print(f'Prazer em te conhecer {nome:>20}!') # print:           Richard!
print(f'Prazer em te conhecer {nome:<20}!') # print: Richard          !
print(f'Prazer em te conhecer {nome:^20}!') # print:     Richard      !
print(f'Prazer em te conhecer {nome:=^20}!') # print:====Richard======!
