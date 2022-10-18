valido = True

while valido == True:
    nota = int(input('Digite uma nota: '))
    if nota >= 0 and nota <= 10:
        print('Nota válida')
        valido = True
    else:
        print('Nota inválida')
        valido = False

print('Fim do programa')