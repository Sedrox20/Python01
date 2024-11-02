def SeuNome():
    nome = []
    notas = []

    for i in range(2):
        nome.append(input('Digite seu nome: '))
        notas.append(input('Digite sua idade: '))

    indexx = notas.index(min(notas))

    print(f'{nome[indexx]} é o mais novo com idade {min(notas)} anos.')

SeuNome()

# --------------------------------

#algoritimo de busca
pessoa = []
for i in range(5):
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade'))
    pessoa.append({'Nome': nome, 'idade':idade})
def buscar():
    i=0
    menor=0
    while(i<5):
        if(pessoa[i]['idade']<pessoa[menor]['idade']):
            menor=i
        else:
            menor=menor
        i+=1
    return menor
print(f'{pessoa[buscar()]}')
