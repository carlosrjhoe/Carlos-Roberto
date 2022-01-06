# Exercício 2 - Reescreva o código abaixo, usando a função map(). O resultado final deve ser o mesmo!

palavras = 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil'.split() # SEPARA OS ESPAÇOS EM BRANCO ENTRE CADA PALAPRA
print(palavras)

resultado = map(lambda a: [a.upper(), a.lower(), len(a)], palavras) # PARA CADA PALAVRA SEPARADA, O MAP FAZ A INTERAÇÃO E COLOCA EM CAIXA ALTA, BAIXA E TRÁS QUANTAS LETRAS TEM EM CADA PALAVRA

for i in resultado:
    print (i)