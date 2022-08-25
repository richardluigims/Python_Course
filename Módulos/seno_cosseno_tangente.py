from math import cos, sin, tan, radians

n1 = float(input('Digite o valor de um ângulo: '))
cos = cos(radians(n1))
sin = sin(radians(n1))
tan = tan(radians(n1))

print(f'Cosseno: {cos:.2f}.\nSeno: {sin:.2f}.\nTangente: {tan:.2f}.')
