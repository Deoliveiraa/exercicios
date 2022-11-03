
subtotal = 0
print('Bem-vindo a Sorveteria do Lucas Rodrigues de Oliveira')
print('--------------------------------------------Cardápio--------------------------------------------')
print('|  Código |      Descrição       |  Tamanho P (500ml) | Tamanho M (1000ml) | Tamanho G (2000ml |')
print('|   TR    | Sabores Tradicionais |      R$ 6,00       |      R$ 10,00      |      R$ 18,00     |')
print('|   ES    |   Sabores Especiais  |      R$ 7,00       |      R$ 12,00      |      R$ 21,00     |')
print('|   PR    |    Sabores Premium   |      R$ 8,00       |      R$ 14,00      |      R$ 24,00     |')
print('------------------------------------------------------------------------------------------------')
while True:
    tamanho = input('Entre com TAMANHO do pote desejado (P/M/G): ')
    codigo = input('Entre com o CÓDIGO do sabor desejado (TR/ES/PR): ')
    tamanho = tamanho.upper()
    codigo = codigo.upper()
    if codigo == 'TR':
        if tamanho == 'P':
            subtotal += 6.00
            print('Você pediu um sorvete sabor TRADICIONAL P de R$ 6,00 ')
            print( '----------------------------------------------------')
            sair = input('Deseja pedir mais alguma coisa? (S/N): ')
            sair = sair.upper()
            if sair == 'N':
                break
            elif sair == 'S':
                continue
            else:
                 print('Você não digitou N para finalizar, qualquer outro caracter segue com o sistema')
        elif tamanho == 'M':
            subtotal += 10.00
            print('Você pediu um sorvete sabor TRADICIONAL M de R$ 10,00')
            print( '----------------------------------------------------')
            sair = input('Deseja pedir mais alguma coisa? (S/N): ')
            sair = sair.upper()
            if sair == 'N':
                break
            else:
                 continue
        elif tamanho == 'G':
            subtotal += 18.00
            print('Você pediu um sorvete sabor TRADICIONAL G de R$ 18,00')
            print( '----------------------------------------------------')
            sair = input('Deseja pedir mais alguma coisa? (S/N): ')
            sair = sair.upper()
            if sair == 'N':
                break
            else:
                 continue
        else:
            print('!!!!!!!  TAMANHO ou CÓDIGO INVÁLIDOS(S)  !!!!!!!')
            continue
    elif codigo == 'ES':
        if tamanho == 'P':
            subtotal += 7.00
            print('Você pediu um sorvete sabor ESPECIAL P de R$ 7,00')
            print( '----------------------------------------------------')
            sair = input('Deseja pedir mais alguma coisa? (S/N): ')
            sair = sair.upper()
            if sair == 'N':
                break
            else:
                 continue
        elif tamanho == 'M':
            subtotal += 12.00
            print('Você pediu um sorvete sabor ESPECIAL M de R$ 12,00')
            print( '----------------------------------------------------')
            sair = input('Deseja pedir mais alguma coisa? (S/N): ')
            sair = sair.upper()
            if sair == 'N':
                break
            else:
                 continue
        elif tamanho == 'G':
            subtotal += 21.00
            print('Você pediu um sorvete sabor ESPECIAL G de R$ 21,00')
            print( '----------------------------------------------------')
            sair = input('Deseja pedir mais alguma coisa? (S/N): ')
            sair = sair.upper()
            if sair == 'N':
                break
            else:
                 continue
        else:
            print('!!!!!!!  TAMANHO ou CÓDIGO INVÁLIDOS(S)  !!!!!!!')
            continue
    elif codigo == 'PR':
        if tamanho == 'P':
            subtotal += 8.00
            print('Você pediu um sorvete sabor PREMIUM P de R$ 7,00')
            print( '----------------------------------------------------')
            sair = input('Deseja pedir mais alguma coisa? (S/N): ')
            sair = sair.upper()
            if sair == 'N':
                break
            else:
                 continue
        elif tamanho == 'M':
            subtotal += 14.00
            print('Você pediu um sorvete sabor PREMIUM P de R$ 14,00')
            print( '----------------------------------------------------')
            sair = input('Deseja pedir mais alguma coisa? (S/N): ')
            sair = sair.upper()
            if sair == 'N':
                break
            else:
                 continue
        elif tamanho == 'G':
            subtotal += 24.00
            print('Você pediu um sorvete sabor PREMIUM P de R$ 24,00')
            print( '----------------------------------------------------')
            sair = input('Deseja pedir mais alguma coisa? (S/N): ')
            sair = sair.upper()
            if sair == 'N':
                break
            else:
                 continue
        else:
            print('!!!!!!!  TAMANHO ou CÓDIGO INVÁLIDOS(S)  !!!!!!!')
            continue
    else:
        print('!!!!!!!  TAMANHO ou CÓDIGO INVÁLIDOS(S)  !!!!!!!')
        continue
print('O total a ser pago é: {:.2f} '.format(subtotal))