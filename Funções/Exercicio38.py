def inf():
    if cidade == ('Rio de janeiro'):
        print(f'Olá {nome}, seja bem vindo à Cidade Maravilhosa')
    else:
        print(f'Olá {nome}, você está em {cidade}')
    return
    
nome = input('Digite seu nome: ')
cidade = input('Digite a cidade em que você está: ')

inf()

    