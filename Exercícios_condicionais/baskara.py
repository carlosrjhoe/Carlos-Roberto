import math

texto = 'BASKARA'
print('#' * 45)
print(texto.center(45))
print('#' * 45)

a = float(input('COEFICIENTE [A]: '))
b = float(input('COEFICIENTE [B]: '))
c = float(input('COEFICIENTE [C]: '))

class baskara():
    def delta(a,b,c):
        return math.pow(b, 2) - 4 * a * c

    def x(a,b,c):
        return (- b + math.sqrt(baskara.delta(a, b, c))) / (2 * a)

    def y(a,b,c):
        return (- b - math.sqrt(baskara.delta(a, b, c))) / (2 * a)


if (a == 0 or baskara.delta(a,b,c) < 0):
    print('A equação não possui raizes reais.')
else:
    print(f'X1 = {baskara.x(a,b,c):.4f}')
    print(f'X2 = {baskara.y(a,b,c):.4f}')

