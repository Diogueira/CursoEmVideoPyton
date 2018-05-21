salario = float(input('qual seu salario?: '))
aumento = salario + (salario * 15 /100)
print('Seu Salario era {:.2f}R$, agora voce vai receber {:.2f}R$ por mês.'.format(salario, aumento))