print('Calculadora de peso Ideal.\n')

sexo = input('Informe seu sexo(m ou f): ').lower()
altura = float(input('Informe sua altura em metros: '))

if sexo == 'm' and altura > 0:    
    peso = (72.7 * altura) -58
    print('O seu peso ideal �:', peso)

elif sexo == 'f' and altura > 0:
    peso = (62.7 * altura) - 44.7
    print('O seu peso ideal �:', peso)

if sexo != 'm' and sexo != 'f':
    print('O sexo informado � inv�lido!')
if altura <= 0:
    print('Altura inv�lida!')
     
        
    

    



    
        


