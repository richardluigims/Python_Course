n1 = float(input('Digite um valor: '))
n2 = float(input('Digite um valor: '))
n3 = float(input('Digite um valor: '))
menor = n1
maior = n1

if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print(f'O maior valor é {maior:.2f}.')
print(f'O menor valor é {menor:.2f}.')
