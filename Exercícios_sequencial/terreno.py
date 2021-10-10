largura = float(input('Largura do terreno: '))
comprimento = float(input('Comprimento do terreno: '))
valor = float(input('Valor do terreno: R$ '))

class terreno():

    def area(largura, comprimento):
        return largura * comprimento

    def preco(area, valor):
        return area(largura, comprimento) * valor

print(f'\nArea do terreno = {terreno.area(largura, comprimento):.2f}m²')
print(f'Preço do terreno = R${terreno.preco(terreno.area, valor):.2f}')

#print(area(largura, comprimento))
#print(preco(area, valor))