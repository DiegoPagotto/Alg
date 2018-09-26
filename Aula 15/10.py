def funcao(x,y):
    if x > y:
        maior = x
        print(f'Entre {x} e {y}, o maior valor é {maior}')
    elif x < y:
        maior = y
        print(f'Entre {x} e {y}, o maior valor é {maior}')
    else:
        print('Os valores são iguais.')
funcao(float(input('Informe um valor: ')),float(input('Informe um valor: ')))
