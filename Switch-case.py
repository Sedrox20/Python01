# value = 0
# match value:
#     case 1:
#         Result = 'one'
#     case 2:
#         Result = 'two'
#     case 3:
#         Result = 'thre'
#     case _:
#         Result = 'default'
# print(Result)

qtd=0
total=0
escolha=0
while(escolha!=5):
     print('Cardápio')
     print('1- Calabresa com cebola - R$ 59,99')
     print('2- Camarão com catupiry - R$ 69,99')
     print('3- Frango com requeijão - R$ 49,99')
     print('4- Chocolate com morango - R$ 39,99')
     print('5- Finalizar pedido')   

     escolha = int(input('Digite a opção escolhida (apenas números): '))
     match escolha:
        case 1:
             print('Calabresa com cebola - R$ 59,99')
             total+=59.9
             qtd+=1
        case 2:
             print('Camarão com catupiry - R$ 69,99')
             total+=69.9
             qtd+=1
        case 3:
             print('Frango com requeijão - R$ 49,99')
             total+=49.9
             qtd+=1
        case 4:
             print('Chocolate com morango - R$ 39,99')
             total+=39.9
             qtd+=1
        case 5:
             print(f'Total do pedido: R${total}, quantidade de pizza = {qtd}')
        case _:
             print('Escolha uma opção válida')
