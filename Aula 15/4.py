def dados(nome, idade):
    nome = nome.capitalize()
    if idade >= 18:
        print(nome,' é maior de idade.')
    else:
        print(nome,' é menor de idade.')
dados(input('Qual seu nome? '),int(input('Qual sua idade? ')))
