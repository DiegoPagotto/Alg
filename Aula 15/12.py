def funcao(valor, desconto):
    final = valor - (desconto * valor)/100
    print(final)
funcao(float(input('Informe o valor do produto: ')),float(input('Informe o valor do desconto: ')))
