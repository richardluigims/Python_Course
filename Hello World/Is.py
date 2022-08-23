n = input('Digite algo: ')

print('O tipo primitivo desse valor é',type(n))
print('É um número?', n.isnumeric())
print('É alfabético?', n.isalpha())
print('É alfanumérico?', n.isalnum()) # letras e números (juntos = 7a), letras ou números
print('Tem apenas espaços?', n.isspace())
print('Está em maiúsculas?', n.isupper())
print('Está em minúsculas?', n.islower())
print('Está capitalizada?', n.istitle()) # maiúsculas e minúsculas
