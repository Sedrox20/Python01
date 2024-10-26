mylist = []
soma = 0

for i in range (10):
    mylist.append(int(input('Digite 10 números para serem somados: ')))
    soma += mylist[i]

print(f'Soma: {soma}\nMédia {soma/len(mylist)}')