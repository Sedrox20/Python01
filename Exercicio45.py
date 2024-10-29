lista = []
contador = 1


for i in range(5):
    lista.append(int(input(f'Digite o {contador}° número: ')))
    contador += 1
    lista.sort()

print(f'Os números são {lista}')