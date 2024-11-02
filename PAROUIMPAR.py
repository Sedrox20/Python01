import random
def game(numero):
    player2=random.randint(0,5)
    print(f'Player1: {numero} vs Player2: {player2}')
    if (numero+player2)%2==0:
        return 'PAR - Player1 venceu'
    else:
        return 'ÍMPAR - Player2 vencer'

print('Jogo - Par ou Ímpar')
print('Números permitidos de 0 a 5')
print()
print('----------------------------------')
print()

jogadas= int(input('Digite quantas vezes você quer jogar: '))

for i in range(jogadas):
    player1 = int(input('Insira sua jogada: '))
    print(f'{game(player1)}')
