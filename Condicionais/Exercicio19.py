print('Digite: pedra, papel ou tesoura')

jogador1 = str(input('Escolha sua opção: '))
jogador2 = str(input('Escolha sua opção: '))

if(jogador1==jogador2):
    print('Empate')
elif((jogador1=='pedra' and jogador2=='tesoura') or (jogador1=='papel' and jogador2=='pedra') or (jogador1=='tesoura' and jogador2=='papel')):
    print(f'O jogador1 venceu!!! ({jogador1} vence de  {jogador2})')
else:
    print(f'O jogador2 venceu!!! ({jogador2} vence de {jogador1})')







