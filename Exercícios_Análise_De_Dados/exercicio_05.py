# Exercício 5 - Abaixo você encontra duas listas. Faça com que cada elemento da listaA seja elevado 
# ao elemento correspondente na listaB.
from math import pow

listaA = [2, 3, 4]
listaB = [10, 11, 12]

print(list(map(pow, listaA, listaB)))
