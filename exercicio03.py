idade = int(input('Qual a idade ? '))
if idade >= 5 and idade <=7:
    print('Infatil A')
elif idade >= 8 and idade <=10:
    print('Infatil B')
elif idade >= 11 and idade <=14:
    print('Juvenil A')
elif idade >= 15 and idade <=17:
    print('Juvenil B')
else:
    print('Idade fora das categorias.')