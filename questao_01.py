print('Digite seus dadaos: \n')

nome = input('Nome:')
sexo = input('Sexo:').lower()
cabelo = input('Cabelo').lower()
altura = int(input('Altura: '))
peso = int(input('Peso: '))

compativel = (sexo == 'feminino'
              and altura >= 155
              and altura <=175
              and peso >= 45
              and peso<= 65
              and cabelo == 'castanho')

print('Ol� M�rcio, a compatibilidade entre voc� e {} �: {}'.format(nome, compativel))
