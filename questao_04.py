salario = float(input('Informe seu sal�rio: '))

if salario < 280:
    reajuste = salario * 0.2
    percentual = 20

if salario > 280 and salario <= 699 :
    reajuste = salario * 0.15
    percentual = 15

if salario > 699 and salario <= 1499:
    reajuste = salario * 0.1
    percentual = 10

if salario >= 1500:
    reajuste = salario * 0.05
    percentual = 5

print('''
Sal�rio antes do reajuste: {}
Percentual do aumento aplicado: {}
Valor do aumento: {}
Sal�rio com reajuste: {}
'''.format(salario, percentual, reajuste, salario+reajuste)) 
