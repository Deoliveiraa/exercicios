valor = float(input('Qual é o valor do produto que deseja aplicar o desconto ? '))
d = float(input('Qual a porcentagem que deseja dar de desconto ? '))
porcentagem = d / 100
resultado = porcentagem * valor
aplicado = valor - resultado
print('O valor aplicado com desconto ficara {}'.format(aplicado))
