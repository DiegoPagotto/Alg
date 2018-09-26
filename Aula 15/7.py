def mes(x):
    meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
    if x >= 1 and x <= 12:
        informado = meses[x-1]
        print('O mês ',x,' é ',informado)
    else:
        print('Mês Inválido')
mes(int(input('Informe um número: ')))
