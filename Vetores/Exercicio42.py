lista = []

for i in range(8):
    lista.append(int(input('Digite um número: ')))
lista.sort()
print(f'O maior é: {lista[len(lista)-1]} e o menor é: {lista[0]}')
