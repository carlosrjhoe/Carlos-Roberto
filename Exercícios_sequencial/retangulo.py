from math import sqrt

base = float(input('Base do retangulo: '))
altura = float(input('Altura do retangulo: '))

class retangulo():

    def area(base, altura):
        return base * altura

    def perimetro(base, altura):
        return 2 * (base + altura)

    def diagonal(base, altura):
        return sqrt(base * base + altura * altura)

print(f'\nAREA = {retangulo.area(base, altura):.4f}')
print(f'PERIMETRO = {retangulo.perimetro(base, altura):.4f}')
print(f'DIAGONAL = {retangulo.diagonal(base, altura):.4f}')
