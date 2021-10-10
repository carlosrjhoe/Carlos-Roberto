import math

r = float(input('Digite o valor de raio do circulo: '))

class circulo():
    def area(r):
        return math.pi * math.pow(r, 2)
        

print(f'AREA = {circulo.area(r):.3f}')