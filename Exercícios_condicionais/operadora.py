texto = 'OPERADORA'
print('#' * 45)
print(texto.center(45))
print('#' * 45)

minutos = int(input('DIGITE A QUANTIDADE DE MINUTOS: '))

plano = 50
multa = 2

if minutos <= 100:
    print(f'VALOR A PAGAR: R${plano}')
else:
    print(f'VALOR A PAGAR: R${((minutos - 100) * multa) + plano:.2f}')

