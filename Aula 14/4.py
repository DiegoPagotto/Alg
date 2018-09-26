str = input('Informe uma palavra: ')
str = str.lower()
tras_frente = str[::-1]
if str == tras_frente:
    print(str,' é um palíndromo')
else:
    print(str,' não é um palíndromo')
 
