texto = 'MENOR DE TRÊS'
print('#' * 45)
print(texto.center(45))
print('#' * 45)

a = int(input('PRIMEIRO VALOR: '))
b = int(input('SEGUNDO VALOR: '))
c = int(input('TERCEIRO VALOR: '))

# PARA ACHAR O MENOR NUMÉRO
def numeros(a,b,c):
    min = a
    if b < min:
        min = b
    elif c < min:
        min = c
    return min

print(f'MENOR = {numeros(a,b,c)}')