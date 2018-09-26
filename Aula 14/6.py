str = input('Informe uma string: ')
anterior = ''
for aux in str:
    L_atual = aux
    anterior = anterior + L_atual
    print(anterior)
