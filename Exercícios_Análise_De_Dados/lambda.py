preco = 500
precos = [100.00, 200.00, 50.00, 80.00, 30.00]

def calcular_imposto(preco):
    return preco * 0.3

#print(calcular_imposto(preco))

#calcular_imposto2 = lambda preco: preco * 0.3
#imposto = list(map(lambda x: round(x * 0.3), precos))

#print(calcular_imposto2(preco))
#print(f'Valor em R${preco:.2f}')
#print(f'{imposto:.2f}')

for i in precos:
    imposto = list(map(lambda i: i * 0.8, precos))
print(precos)
print(f'{imposto}')