# ordem de precedência

# 1 - ()
# 2 - ** - potências
# 3 - *,/,//,%
# 4 - +,-

n1 = int(input('valor 1: '))
n2 = int(input('valor 2: '))
soma = n1 + n2 #soma
mult = n1 * n2 #multiplicação
div = n1 / n2 #divisão float
divInt = n1 // n2 #divisão inteira
pot = n1 ** n2 #potência
resto = n1 % n2 #resto da divisão
Rq1 = n1**(1/2) #raíz quadrada
Rq2 = n2**(1/2)

print(f'Soma: {soma}. Produto: {mult}. Divisão: {div:.2f}.', end=' ') #end adiciona algo no fim da linha e impede que ela quebre
print(f'Divisão inteira: {divInt}. Potência: {pot}')
print(f'A raíz quadrada do primeiro é {Rq1:.2f}, e do segundo é {Rq2}')
