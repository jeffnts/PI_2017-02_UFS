pacote = input('Informe o tipo de pacote: ').lower()
forma_pagamento = input('Informe a forma de pagamento: ').lower()

#Define o desconto igual a zero para evitar erro por falta de atribuição a viriável
desconto = 0

#Transforma as palavras com acento em palavras sem acento da variável pacote
if pacote == 'básico':
    pacote = 'basico'
    
#Transforma as palavras com acento em palavras sem acento da variável forma_pagamento    
if forma_pagamento == 'débito automatico':
    forma_pagamento = 'debito automatico'
    
if forma_pagamento == 'débito automático':
    forma_pagamento = 'debito automatico'
    
if forma_pagamento == 'debito automático':
    forma_pagamento = 'debito automatico'

#Compara os pacotes, aplica o desconto e adiciona os canais, caso o pagamento seja através de débito automático.
if pacote == 'basico' and forma_pagamento == 'debito automatico':
    valor = 80.8
    canais = 32 + 6
    desconto = valor *0.05

elif pacote == 'basico' and forma_pagamento !=('debito automatico'):
    valor = 80.8
    canais = 32

if pacote == 'entreterimento' and forma_pagamento == 'debito automatico':
    valor = 100
    canais = 55 + 6
    desconto = valor *0.05

elif pacote == 'entreterimento' and forma_pagamento !=('debito automatico'):
    valor = 100
    canais = 32

if pacote == 'multicultural' and forma_pagamento == 'debito automatico':
    valor = 130.23
    canais = 70 + 11
    desconto = valor * 0.10

elif pacote == 'multicultural' and forma_pagamento !=('debito automatico'):
    valor = 130.23
    canais = valor * 0.10

if pacote == 'completo' and forma_pagamento == 'debito automatico':
    valor = 215.5
    canais = 112 + 11
    desconto = valor *0.10

elif pacote == 'completo' and forma_pagamento !=('debito automatico'):
    valor = 80.8
    canais = 112

print('''
Valor da mensalidade com o reajuste: {}
Quantidade total de canais: {}
'''.format(valor-desconto, canais))
    
    
