from math import sqrt

base = float(input('Base do retangulo: '))
altura = float(input('Altura do retangulo: '))

def area(base, altura):
    return base * altura

def perimetro(base, altura):
    return 2 * (base + altura)
    
# FALTA CALCULAR DIAGONAL
def diagonal(base, altura):
    return 

print(f'\nAREA = {area(base, altura):.4f}')
print(f'PERIMETRO = {perimetro(base, altura):.4f}')