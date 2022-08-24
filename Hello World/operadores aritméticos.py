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
pot = n1 ** n2 #potência. também pode ser pow(n1,n2)
resto = n1 % n2 #resto da divisão

print(f'Soma: {soma}. Produto: {mult}. Divisão: {div:.2f}.', end=' ') #end = comando para não pular linha (dar um 'espaço' nas aspas simples para não grudar). Pode usar outros comandos tbm ---> end='>>>'
print(f'Divisão inteira: {divInt}. Potência: {pot}')                  #end adiciona algo no fim da linha, e impede q ela seja quebrada
