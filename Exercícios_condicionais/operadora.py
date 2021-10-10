texto = 'OPERADORA'
print('#' * 45)
print(texto.center(45))
print('#' * 45)

minutos = int(input('DIGITE A QUANTIDADE DE MINUTOS: '))

plano = 50.00
multa = 2

class operadora():
    def valorApagar(minutos):
        return ((minutos - 100) * 2) + plano

if minutos < 100:
    print(f'VALOR A PAGAR = R${plano:.2f}')
else:
    print(f'VALOR A PAGAR = R${operadora.valorApagar(minutos):.2f}')