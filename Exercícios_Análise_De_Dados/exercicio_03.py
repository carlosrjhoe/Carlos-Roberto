# Exercício 3 - Calcule a matriz transposta da matriz abaixo.
# Matriz transposta é um conceito fundamental na construção de redes neurais artificiais, base de sistemas de IA.

matrix = [[1, 2],[3,4],[5,6],[7,8]]
transpose = [[row[i] for row in matrix] for i in range(2)]  # SEPARA A QUANTIDADE DE LISTAS DENTRO DE LISTA EM APENAS 2 LISTAS, ADICIONADO O VALOR DO 1° INDICE NA LISTA, E VALOR DO DO 2° INDICE EM OUTRA LISTA.
print(transpose)