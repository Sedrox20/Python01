nomes = []
listamedia = []

def dados():
    for i in range(2):
        nome = input('Digite o nome do aluno(a): ')
        nomes.append(nome)
        
        media = int(input('Digite a média do aluno(a): '))
        while media < 0 or media > 10:
            media = int(input('Digite uma média válida (0 a 10): '))

        listamedia.append(media)

    return

dados()
print(f'Nomes: {nomes} e Médias: {listamedia}')