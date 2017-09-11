idade = 12
if idade < 4:
	preço = 0
elif idade < 18:
    preço = 5
else:
    preço = 10
print('Seu custo de admissao é $' + str(preço) + '.')
#a condiçoes foram dadas de acordo cada idade, cm o valor da variavel foi de 12, a condiçao
#para esse valor era de $5, entao foi concatenado a mensagem e o condiçao que se encaixou no valor da variavel.