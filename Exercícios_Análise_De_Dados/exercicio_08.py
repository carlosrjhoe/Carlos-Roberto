# Exercício 8 - Considere o código abaixo. Obtenha o mesmo resultado usando o pacote time. 
# Não conhece o pacote time? Pesquise!

import datetime
print (datetime.datetime.now().strftime("%d/%m/%Y %H:%M"))  # Retorna uma string representando a data, controlada por uma string de formato explícito.

import time
print (time.strftime("%d/%m/%Y %H:%M")) # retorna um tempo idealizado , independente de qualquer dia em particular, supondo que todo dia tenha exatamente 24 * 60 * 60 segundos.