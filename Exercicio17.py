peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura*altura)
print(f'Seu IMC é: {imc}')

if (imc>25):
    print('Acima do peso ideal')
else:
    print('Peso ok')

