altura = float(input('qual a altura?: '))
largura = float(input('qual a largura?: '))
área = largura * altura
print('sua parede tem a dimenção de {}x{} e sua área é de {}m².'.format(largura, altura, área))
tinta = área / 2
print('para pintar a área vai precisar de {:.2f}Litros de tinta.'.format(tinta))