str = input('Informe uma string: ')
letra = input('Informe a letra: ')
vezes = str.count(letra)
while vezes > 0:
    for aux in range(0,len(str)):
        primeira = str.index(letra)
        começo = str[0:primeira]
        final = str[primeira+1:len(str)]
    str = começo + final
    vezes = vezes - 1
print(str)
