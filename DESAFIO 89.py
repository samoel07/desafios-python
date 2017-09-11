lista_p = ['calabresa', 'tomate', 'ovo', 'frango', 'batata frita']
lista_d = ['tomate', 'frango', 'batata frita', 'mussarela']
for lista_ds in lista_d:
    if lista_ds in lista_p:
        print('Adicionando ' + lista_ds + '.')
    else:
        print('Nao temos ' + lista_ds + ' no momento.')