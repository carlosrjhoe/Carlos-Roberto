class mercado():

    def troco(dinheiro, quantidade, preco):
        return dinheiro - quantidade * preco

preco = float(input('Preço unitário do produto: '))
quantidade = int(input('Quantidade comprada: '))
dinheiro = float(input('Dinheiro recebido: '))


print(f'TROCO = {mercado.troco(dinheiro, quantidade, preco)}')