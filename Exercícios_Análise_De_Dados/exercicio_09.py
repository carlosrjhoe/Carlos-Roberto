# Exercício 9 - Considere os dois dicionários abaixo. 
# Crie um terceiro dicionário com as chaves do dicionário 1 e os valores do dicionário 2.

dict1 = {'a':1,'b':2}
dict2 = {'c':4,'d':5}

def trocaValores(d1, d2):
    dicTemp = {}
    
    for d1key, d2val in zip(d1,d2.values()):    # PEGA O VALOR DA CHAVE DA 2 DICIONARIO E SUBSTITUI A DO 1 DICIONARIO EM OUTRO DICIONARIO.
        dicTemp[d1key] = d2val
    
    return dicTemp

dict3 = trocaValores(dict1, dict2)
print(F'DICIONARIO 1°{dict1}')
print(F'DICIONARIO 2°{dict2}')
print(F'DICIONARIO 3°{dict3}')