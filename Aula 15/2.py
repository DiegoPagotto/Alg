def dados():
    nome = input('Qual seu nome? ').capitalize()
    idade = int(input('Qual sua idade? '))
    if idade >= 18:
        print(nome,' é maior de idade.')
    else:
        print(nome,' é menor de idade.')
dados()
