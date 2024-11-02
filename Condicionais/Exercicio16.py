# valor1 = int(input('Digite o primeiro número: '))
# valor2 = int(input('Digite o segundo número: '))
# valor3 = int(input('Digite o terceiro número: '))

# if(valor1>valor2):
#     if(valor1>valor3):
#         print(f'O maior número é o {valor1}')
#     else:
#         print(f'O maior número é {valor3}')
# elif(valor2>valor3):
#     print(f'O maior número é {valor2}')

# else:
#     if(valor1 == valor2 == valor3):
#         print('Os números são iguais')

#     else:
#         print(f'O maior número é {valor3}')

# ---------------------------------------------------------------------------------------------------------------------

# valor1 = int(input('Digite o primeiro número: '))
# valor2 = int(input('Digite o segundo número: '))
# valor3 = int(input('Digite o terceiro número: '))

# if(valor1==valor2==valor3):
#     print('os 3 valores são iguais')

# elif(valor1>valor2 and valor1>valor3):
#     print(f'O maior número é {valor1}')
# elif(valor2>valor3):
#     print(f'O maior número é {valor2}')

# else:
#     print(f'O maior número é {valor3}')
 
#--------------------------------------------------------------------------------------------------------------------------

valor1 = int(input('Digite o primeiro número: '))
valor2 = int(input('Digite o segundo número: '))
valor3 = int(input('Digite o terceiro número: '))

valores=[valor1,valor2,valor3]
valores.sort()
valores.reverse()
print(f'O maior número é {valores[0]}')
       






