n1 = str(input('Digite o seu nome completo: ')).strip()

print(n1.upper())
print(n1.lower())
print(len(n1))
print(len(n1)-n1.count(' '))
print(n1.find(' '))

split = n1.split()
print(len(split[0]))
