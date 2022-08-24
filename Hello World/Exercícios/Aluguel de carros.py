Km = float(input('Digite os Km percorridos pelo cliente: '))
Dias = float(input('Digite a quantidade de dias de aluguel: '))
preço = (60*Dias) + (0.15*Km)

print(f'O preço a pagar é R${preço:.2f}.')
