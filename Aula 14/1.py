str = input('Informe uma string: ')
letra = input('Informe a letra: ')
for aux in range(0,len(str)):
    primeira = str.find(letra)
    começo = str[0:primeira]
    final = str[primeira+1:len(str)]
sem_letra = começo + final
print(sem_letra)
