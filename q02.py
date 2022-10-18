nome = input('Usuário: ')

senha = input('Senha: ')

while senha == nome: # condição de repetição
   print('A senha não pode ser igual ao nome do usuário!')
   senha = input('Senha: ')

 #caso a condição de execução seja falsa (continua)
else:
   print('Informações foram cadastradas com sucesso!')