def funcao(distancia,valor):
    lucro = distancia * valor
    print(f'O taxista receberá R${lucro} por percorrer {distancia}km, com cada quilômetro custando R${valor}')
funcao(float(input('Qual a distância percorrida? ')),float(input('Qual o valor por quilômetro? ')))
