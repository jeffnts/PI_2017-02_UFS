ano = int(input('Digite o ano:'))

if ano % 4 == 0:
    if ano % 100 == 0 and not(ano % 400 == 0):
        print(ano, ' n�o � um ano bissesto!')
    print(ano, ' � um ano bissesto!')
else:
    print(ano, ' n�o � um ano bissesto!')
    
