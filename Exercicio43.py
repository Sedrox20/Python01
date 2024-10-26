lista = []
contador = 1
cont = 0

for i in range(10):
    lista.append(int(input(f'Digite o {contador}° número: ')))
    contador += 1

    if (lista[i] > 10):
        cont+=1
        print(lista[i])

print(cont)

    
