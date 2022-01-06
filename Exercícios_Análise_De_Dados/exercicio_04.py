# Exercício 4 - Crie duas funções, uma para elevar um número ao quadrado e outra para elevar ao cubo. 
# Aplique as duas funções aos elementos da lista abaixo. 
# Obs: as duas funções devem ser aplicadas simultaneamente.
from math import pow    # IMPORTA A FUNÇÃO POW DA BIBLIOTECA MATH

lista = [2, 4, 7, 9, 21]    # LISTA COM E5 LEMENTOS

def quadrado(x):    # CRIA UMA FUNÇÃO PARA ELEVAR UM VALOR AO QUADRADO
    return pow(x, 2)

def cubo(x):    # CRIA UMA FUNÇÃO PARA ELEVAR UM VALOR AO CUBO
    return pow(x, 3)

func = [quadrado, cubo] # CRIAR UMA LISTA COM AS DUAS FUNÇOES ANTES CRIADA

for i in lista: # FAZ CORRER I EM CADA VALOR EM LISTA
    valor = map(lambda x: x(i), func)   
    print(list(valor))