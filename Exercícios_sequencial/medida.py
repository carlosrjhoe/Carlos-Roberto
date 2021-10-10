import math

a = float(input('DIGITE A MEDIDA [A]: '))
b = float(input('DIGITE A MEDIDA [B]: '))
c = float(input('DIGITE A MEDIDA [C]: '))

class formas():
    def quadrado(a):
        return math.pow(a, 2)

    def triangulo(a, b):
        return (a * b) / 2

    def trapezio(a, b, c):
        return ((a + b) * c) / 2

print(f'AREA DO QUADRADO = {formas.quadrado(a):.4f}')
print(f'AREA DO TRIANGULO = {formas.triangulo(a, b):.4f}')
print(f'AREA DO TRAPEZIO = {formas.trapezio(a, b, c):.4f}')
