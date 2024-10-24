salario = int(input('Digite o valor do seu salario: '))

valorVT = (6 / 100)*salario
valorPS = (3 / 100)*salario

salariofinal = salario - (valorVT + valorPS)

print (f'O seu desconto do vale transporte é de: R$ {valorVT}')
print (f'O seu desconto do plano de saúde é de: R$ {valorPS}')
print (f'O salario final será: R$ {salariofinal}')