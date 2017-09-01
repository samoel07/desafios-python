pessoas = ['samoel', 'carlos', 'joao']
for pessoas in pessoas:
	print(pessoas.title(), 'voce sabe a prova?')
print('entao voce poderia mim ajudar, ' + pessoas.title())
#no caso da ultima msg aparecer somente para o ultimo elemento, é por que ela esta fora do loop,
# entao ela sõ vai interagir cm o ultimo elemento.