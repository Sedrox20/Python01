nome = str(input('Digite um nome válido: '))

while (len(nome) <3):
   nome = str(input('Digite um nome válido: '))
else:
   print(f'Nome registrado {nome}')


idade = int(input('Digite uma idade válida: '))

while (idade > 150 or idade < 0):
   idade = int(input('Digite uma idade válida: '))
else:
   print(f'Idade registrada {idade}')


salario = int(input('Digite um salário válido: '))

while (salario <= 0):
   salario = int(input('Digite uma salário válido: '))
else:
   print(f'Salário registrado R$ {salario}')
   

sexo = str(input('Digite seu sexo: '))

while (sexo != 'f'and sexo != 'm' ):
   sexo = str(input('Digite seu sexo: '))
else:
   print(f'Seu sexo é {sexo}')


civil = str(input('Digite seu estado civil: '))

while (civil != 's' and civil !='c' and civil !='v' and civil !='d'):
   civil = str(input('Digite seu estado civil: '))
else:
   print(f'Seu estado civil é {civil}')

print(f'Suas informações são:\n Nome: {nome}\n Idade: {idade}\n Salário: {salario}\n Sexo: {sexo}\n Estado Cívil: {civil}')


  