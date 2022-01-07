# Exercício 10 - Considere a lista abaixo e retorne apenas os elementos cujo índice for maior que 5.
lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for i, valor in enumerate(lista):   # PERCORRE O VALOR DE CADA INDICE DA LISTA
    if i <= 5:  # VERIFICA CADA INDICE DENTRO DO LOOP, SE FOR MENOR QUE 5, PASSA O LOOP SEM IMPRIMIR NADA
        continue
    else:   # SE O VALOR DO INDICE FOR MAIOR QUE 5, IMPRIME O VALOR DO INDICE.
        print(valor)

# AQUI A MESMO IDEIA, NSESSE CASO SE FOR MAIOR QUE 2, IMPRIME NA TELA.
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
for i, valor in enumerate(seasons):
    if i >= 2:
        print(valor)

print(list(enumerate(seasons)))