ano = int(input('Digite o ano:'))

if ano % 4 == 0:
    if ano % 100 == 0 and not(ano % 400 == 0):
        print(ano, ' não é um ano bissesto!')
    print(ano, ' é um ano bissesto!')
else:
    print(ano, ' não é um ano bissesto!')
    
