numero = -1
#enquanto o usuário não digitar um número entre 0 e 10
print('='*8)
print('TABUADA')
print('='*8)

numero = int(input('Digite um numero: '))
while numero < 0 or numero > 10: #condição loop
    print('Digite um número inválido, digite um valor entre 0 e 10')
    numero = int(input('Digite um numero: '))

    #quando o usuário digita um número válido

#while
#fator = 0
#while fator <= 10:
#    print(f'{numero} x {fator} = {numero * fator}')
#    fator = fator + 1

#for
for fator in 0,1,2,3,4,5,6,7,8,9,10:
    print(f'{numero} x {fator} = {numero * fator}')

print('='*15)
print('Fim do programa')
print('='*15)


