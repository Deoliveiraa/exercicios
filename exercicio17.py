import re

# melhoria do trabalho.py 

subtotal = 0

def calculo():
    global subtotal
    while True:
        nota = float(input("Vamos Caluclar a media das suas notas \n"
                            'Entre com o valor da nota tirado: '))
        porcentagem = float(input('Entre com o valor da porcentagem da nota: '))
        resultado = (porcentagem / 100 ) * nota 
        subtotal += resultado 
        sair = input('Deseja Calcular mais alguma nota ?')
        if (sair.lower() == 'sim') or (sair.lower() == 's'):
            continue
        elif (sair.lower() == 'nao') or (sair.lower() == 'n'):
            return
        else:
            print('Apenas sim para continuar ou não para sair')


# Main
calculo()
print('a media de suas notas são: {}'.format(subtotal))