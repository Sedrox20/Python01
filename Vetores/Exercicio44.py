lista = []
contador = 1
cont = 0
cont2 = 0

for i in range(7):
    lista.append(int(input(f'Digite o {contador}° número: ')))
    contador += 1

    if (lista[i]%2==0):
        cont+=1
        print(lista[i])
    else:
        cont2+=1
        print(lista[i])
   
        
print(f'São {cont} pares e {cont2} ímpares')