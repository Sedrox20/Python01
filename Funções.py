# def saudacao(nome):
#     return f'Olá, {nome}!'

# nome_usuario = input('Qual é o seu nome')
# print(saudacao(nome_usuario))

def Media(n1,n2,n3,n4):
    media = (n1+n2+n3+n4)/4
    if(media>7):
        return f" Aprovado com {media}"
    elif(media<7 and media>4):
        return f"Em recuperação com {media}"
    else:
        return f"Reprovado com {media}"
    
def DefineMedia(nome):
    
    notas = []
    for i in range (4):
        notas.append(float(input(f'Digite a {i+1}° nota: ')))
    print(f'O aluno está {Media(notas[0], notas[1],notas[2],notas[3])}')

for i in range(5):
    nomeAluno=input('Digite o nome do aluno: ')
    DefineMedia(nomeAluno)

    
