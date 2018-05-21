real = float(input('quantos reais voce tem na carteira? R$ '))
dolar = real / 3.70
euro = real / 4.35
print('com seus {:.2f} R$ voce pode comprar apenas US${:.2f} dolares ou {:.2f}£.'.format(real, dolar, euro,))
