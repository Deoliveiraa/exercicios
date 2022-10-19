### escreva um progama que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. calcule o preçoa pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado 
###

km = int(input('Qual foi a quantidade de KM percorridos? '))
dias = int(input('Qual foi a quantidade de dias?  '))

preco = 60 * dias  + 0.15 * km 
print('km {}  dias {}  '.format(km,dias))
print(' Valor a ser pago: {} '.format(preco))