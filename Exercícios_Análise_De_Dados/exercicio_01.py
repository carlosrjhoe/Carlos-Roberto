# Exercício 1 - Crie uma lista de 3 elementos e calcule a terceira potência de cada elemento.

from math import pow    # IMPORTA A FUNÇÃO POW DA BIBLIOTECA MATH
num1 = [3, 5, 7, 9];    # LISTA JÁ COM VALORES
num2 = []   # LISTA VAZIA
print(num1)

for i in num1:  # PERCORRE OS VALORES DENTRO DA LISTA
    num2.append(pow(i, 3))  # ADICIONA OS VALORES DA POSIÇÃO NUM1[I], E ELEVA A 3 POTENCIA, E ADICIONA EM UMA NOVA LISTA.

print(num2)