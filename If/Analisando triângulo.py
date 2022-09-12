print("Vamos montar um triângulo!")
a = float(input("\nDigite o valor do lado A: "))
b = float(input("Digite o valor do lado B: "))
c = float(input("Digite o valor do lado C: "))

if a < b + c and b < a + c and c < a + b:
    print("Triângulo formado!")
else:
    print("Os segmentos digitados não formam um triângulo!")
