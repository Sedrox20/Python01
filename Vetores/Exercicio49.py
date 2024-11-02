nome = []
cidade = []

def dados():
    for i in range(3):
        nome.append(input(f'Digite o {i+1}° nome: '))
        cidade.append(input(f'Digite o {i+1}° cidade: '))

        nome.sort()
        cidade.sort()
    print(nome)
    print(cidade)
    return

dados()
