# contagem de notal ( caixa eletronico ) 

valor = int(input('Digite o valor que deseja sacar: '))
while True:
    if valor >= 200:
        cedulas200 = valor // 200
        valor -= cedulas200 * 200
        print('Cedulas de 200: {}'.format(cedulas200))
        if not valor:
            break
    if valor >= 100:
        cedulas100 = valor // 100
        valor -= cedulas100 * 100
        print('Cedulas de 100: {}'.format(cedulas100))
        if not valor:
            break
    if valor >= 50:
        cedulas50 = valor // 50
        valor -= cedulas50 * 50
        print('Cedulas de 50: {}'.format(cedulas50))   
        if not valor:
            break     
    if valor >= 20:
        cedulas20 = valor // 20
        valor -= cedulas20 * 20
        print('Cedulas de 20: {}'.format(cedulas20))
        if not valor:
            break
    if valor >= 10:
        cedulas10 = valor // 10
        valor -= cedulas10 * 10
        print('Cedulas de 10: {}'.format(cedulas10)) 
        if not valor:
            break
    if valor >= 5:
        cedulas5 = valor // 5
        valor -= cedulas5 * 5
        print('Cedulas de 5: {}'.format(cedulas5))   
        if not valor:
            break
    if valor >= 1:
        cedulas1 = valor // 1
        valor -= cedulas1 * 1
        print('Cedulas de 1: {}'.format(cedulas1))
        break