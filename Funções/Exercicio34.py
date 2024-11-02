# def ProgramasInfantis():
#     lista1=['Peppa Pig', 'Chaves', 'Pantera cor de Rosa', 'Tome e Jerry']
#     print(lista1)
#     return

# def Carros():
#     lista2=['Astra = R$ 30,000', 'Jeep Renegade = R$ 120,000', 'Mobi = R$ 70,000']
#     print(lista2)
#     return

# idade = int(input('Digite sua idade: '))
# if (idade>=18):
#     Carros()
# else: 
#     ProgramasInfantis()

    
def carros():
    carro=[
        {
        "Modelo": "Hb20",
        "Preço": 100000        
    },
    {   
        "Modelo": "Argo",
        "Preço": 90000
    },
    {   
        "Modelo": "Mobi",
        "Preço": 70000
    }
    ]

    for c in carro:
        print(f'{c["Modelo"]}: R$ {c["Preço"]}')
    return

def Programasinfantis():
    lista2=['Peppa','Bolofofos']
    print(lista2)
    return

idade = int(input('Digite sua idade: '))
if (idade>=18):
    carros()
else: 
    Programasinfantis()