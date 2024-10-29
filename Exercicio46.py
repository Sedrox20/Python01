nome = []
nota = []
cont1 = 1
cont2 = 1

for i in range(5):
    nome.append(input(f'Digite o nome do {cont1}° Aluno(a): '))
    cont1 += 1
    nota.append(int(input(f'Digite a média do {cont2}° Aluno(a): ')))
    cont2 += 1

