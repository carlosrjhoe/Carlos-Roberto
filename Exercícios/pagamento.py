nome = str(input('NOME: '))
vHora = float(input('VALOR POR HORA: '))
hTrabalhada = int(input('HORAS TRABALHADAS: '))

def horaExtra(vHora, hTrabalhada):
    return vHora * hTrabalhada
    

print(f'O pagamento para {nome} deve ser de R${horaExtra(vHora, hTrabalhada):.2f}')