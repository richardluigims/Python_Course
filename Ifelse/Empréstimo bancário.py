#O empréstimo é negado se o valor da parcela ultrapassar 30% do salário do cliente

valorEmp = float(input('Valor do empréstimo: '))
salCliente = float(input('Salário do cliente: '))
anos = int(input('Em quanto tempo será pago? '))
pag = valorEmp/(anos*12)

if pag > salCliente*30/100:
    print('Empréstimo negado.')
else:
    print(f'Empréstimo aprovado! Valor da prestação: R${pag:.2f}')
