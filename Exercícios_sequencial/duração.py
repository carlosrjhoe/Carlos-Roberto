duracao = int(input('DIGITE A DURAÇÃO EM SEGUNDOS: '))

class tempo():
    
    # PARA ACHAR HORA
    def hora(duracao):
        return duracao // 3600
    
    # ACHAR O RESTO DA DIVISÃO DA HORA
    def resto(duracao):
        return duracao % 3600

    # PARA ACHAR OS MINUTOS
    def minuto(resto):
        return resto(duracao) // 60

    # PARA ACHAR OS SEGUNDOS
    def seguundos(resto):
        return resto(duracao) % 60

print(f' {tempo.hora(duracao)} HORAS : {tempo.minuto(tempo.resto)} MINUTOS : {tempo.seguundos(tempo.resto)} SEGUNDOS')