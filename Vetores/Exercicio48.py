# def SeuNome():
#     nome = []
#     telefone = []
#     cidade = []

#     for i in range(2):
#         nome.append(input(f'Digite o {i+1}° nome: '))
#         telefone.append(input(f'Digite o {i+1}° telefone: '))
#         cidade.append(input(f'Digite o {i+1}° cidade: '))

#     cidadeCG = cidade.index('Campo Grande')

#     print(f'O {nome[cidadeCG]}, que mora na cidade {cidade[cidadeCG]} e tem o telefone {telefone[cidadeCG]}. ')

# SeuNome()


lista = []

def dados():
    for i in range(2):
        nome = (input(f'Digite o {i+1}° nome: '))
        telefone = (input(f'Digite o {i+1}° telefone: '))
        cidade = (input(f'Digite o {i+1}° cidade: '))

        lista.append({'Nome': nome, 'Telefone': telefone, 'Cidade': cidade})
    return


def buscar():
    i = 0
    while (i<len(lista)):
        if (lista[i]["Cidade"] == "Campo Grande"):
            print(lista[i])

        i += 1
        return

dados()
buscar()

      
      