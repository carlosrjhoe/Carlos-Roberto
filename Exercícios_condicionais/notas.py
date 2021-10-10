texto = 'MÉDIA DAS NOTAS'
print('#' * 45)
print(texto.center(45))
print('#' * 45)

nota1 = float(input('DIGITE A 1 NOTA: '))
nota2 = float(input('DIGITE A 2 NOTA: '))

class semestre():
    def media(nota1, nota2):
        return nota1 + nota2

if (semestre.media(nota1, nota2) < 60.00):
    print(f'NOTA FINAL = {semestre.media(nota1, nota2)}')
    print('REPROVADO')
else:
    print(f'NOTA FINAL = {semestre.media(nota1, nota2)}')

