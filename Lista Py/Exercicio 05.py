
populacao_A = 80000  
populacao_B = 200000  
taxa_crescimento_A = int(input('Digite a taxa de crescimento da população A: '))
taxa_crescimento_B = int(input('Digite a taxa de crescimento população B: '))   


anos = 0


while populacao_A < populacao_B:

    populacao_A *= (1 + taxa_crescimento_A)
    populacao_B *= (1 + taxa_crescimento_B)
    anos += 1  


print(f'{taxa_crescimento_A} , {taxa_crescimento_B} ')
print(f"A população do país A ultrapassará ou igualará a do país B em {anos} anos.")
print(f'A população A terá {populacao_A} habitantes e a B terá {populacao_B} habitantes')