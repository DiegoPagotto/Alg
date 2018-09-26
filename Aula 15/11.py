def funcao(x,y,z):
    if x > y and x > z:
        maior = x
        print(f'Entre {x}, {y} e {z} o maior valor é {maior}')
    elif y > x and y > z:
        maior = y
        print(f'Entre {x}, {y} e {z} o maior valor é {maior}')
    elif z > x and z > y:
        maior = z
        print(f'Entre {x}, {y} e {z} o maior valor é {maior}')
    else:
        print('Os valores são iguais.')
v1=float(input('Informe um valor: '))
v2=float(input('Informe um valor: '))
v3=float(input('Informe um valor: '))
funcao(v1,v2,v3)
