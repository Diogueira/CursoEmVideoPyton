preco = float(input('Quanto vale este produto?: '))
desconto = preco - (preco * 5 / 100)
print('Seu produto custará {:.2f}.'.format(desconto))