idade = 12
if idade < 4:
	preço = 0
elif idade < 18:
    preço = 5
elif idade < 65:
    preço = 10
if idade >= 65:
    preço = 5
print('Seu custo de admissao é $' + str(preço) + '.')