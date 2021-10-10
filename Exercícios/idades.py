# COMEÇAR A FAZER

print('Dados da 1 pessoa:')
nome1 = str(input('NOME: '))
idade1 = int(input('IDADE: '))

print('Dados da 2 pessoa:')
nome2 = str(input('NOME: '))
idade2 = int(input('IDADE: '))

class idade():

    def media(idade1, idade2):
        return idade1 + idade2 / 2

print(f'A idade média de {nome1} e {nome2} é de {idade.media(idade1, idade2)}')
