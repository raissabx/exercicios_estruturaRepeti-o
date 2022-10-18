#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

nome = input('Digite seu nome: ')
while len(nome) < 3:
    print('Digite um nome que contenha pelo menos 3 caracteres: ')
    nome = input('Digite novamente seu nome: ')

idade = int(input('Digite sua idade: '))
while idade < 0 or idade > 150:
    print('A sua idade deve ser de 0 a 150 anos')
    idade = int(input('Digite sua idade novamente: '))

salario = float(input('Digite seu salário: '))
while salario <= 0:
    print('O seu salário deve ser maior que 0')
    salario = input('Digite seu salário novamente: ')

sexo = input('Digite seu sexo: ')
while sexo.upper() != 'F' and sexo.upper() != 'M':
    print('Gênero inválido')
    sexo = input('Digite novamente seu sexo: ')

estado_civil = input('Digite seu estado civil (C, S, D ou V): ')
while estado_civil.upper() != 'C' and estado_civil.upper() != 'S' and estado_civil.upper() != 'D' and estado_civil.upper() != 'V':
    print('Estado civil inválido')
    estado_civil = input('Digite novamente: ')

print(nome, idade, sexo, salario, estado_civil, sep=',')