str1 = input('Informe uma string: ')
str2 = input('Informe uma string: ')
str1 = str1.lower()
str2 = str2.lower()
aux = 0
if len(str1) == len(str2) and aux == 0:
    for x in str1:
        if x not in str2:
            aux +=1
    print('É anagrama')
else:
    print('Não é anagrama')
