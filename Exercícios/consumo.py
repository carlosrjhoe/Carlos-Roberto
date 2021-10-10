

distancia = int(input('DISTACIA PERCORRIDA: '))
combustivel = float(input('COMBUSTÍVEL GASTO: '))

class transporte():
    def consumo(distancia, combustivel):
        return distancia / combustivel

print(f'CONSUMO MÉDIO = {transporte.consumo(distancia, combustivel):.3f}')