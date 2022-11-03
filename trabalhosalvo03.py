#----------começo da função metragem--------------
from email.charset import add_charset
import re


def metragem_limpeza():
    print('-------------------------- MENU 1 de 3 -------------------------------')
    while True:
        try:
            metragem_limpeza = float(input('Entre com a metragem da casa: '))
            if (metragem_limpeza >=30) and (metragem_limpeza <300):
                print('Seram necessários(as) dois(duas) funcionários(as) para a limpeza')
                print('****************************************************************************')
                return metragem_limpeza * 3 + 60
            elif (metragem_limpeza >=300) and (metragem_limpeza <=700):
                print('Seram necessários(as) dois(duas) funcionários(as) para a limpeza')
                print('****************************************************************************')  
                return metragem_limpeza * 0.5 + 120  
            else:
                print('!! Não aceitamos casas com metragem menor que 30m² ou maior que 700m² !!')    
                continue
        except ValueError:
            print('Apenas numeros e numeros com ponto ')    
#----------fim da função metragem-----------------

#----------começo da função tipo de limpeza-------
def tipo_limpeza():
    print('-------------------------- MENU 2 de 3 -------------------------------')
    while True:
        tipo_limpeza = input('Entre com o tipo de Limpeza: \n' +
                             'B - Básica - indicada para sujeiras semanais ou quinzenais \n' +
                             'C - Completa (30% a mais) - indicada para sujeiras antigas e/ou não rotineiras \n')
        tipo_limpeza = tipo_limpeza.upper()
        tipo_limpeza = tipo_limpeza.strip()
        if (tipo_limpeza == 'B'):
            print('Você selecionou a limpeza BAÁSICA')
            print('****************************************************************************')
            return 1.00
        elif (tipo_limpeza == 'C'):
            print('Você selecionou a limpeza COMPLETA') 
            print('****************************************************************************')
            return 1.30
        else:
            print('!!!!!!! Opção Inválida !!!!!!')  
            continue

#----------fim da função tiopo de limpeza---------


#----------começo da função adicional limpeza-----
def adicional_limpeza():
    print('-------------------------- MENU 3 de 3 -------------------------------')
    acumulador = 0
    while True:
        adicional_limpeza = input('Deseja mais algum adicional: \n' + 
                                  '0 - não deseja mais nada (encerrar) \n' +
                                  '1 - passar 10 peças de roupas - 10  \n' +
                                  '2 - Limpeza de 1 Forno/Micro-ondas - 12 \n' +
                                  '3 - Limpeza de 1 geladeira/Freezer - 20 \n' +
                                  '>>> ')
        if (adicional_limpeza == '1'):
            acumulador += 10
            continue
        elif (adicional_limpeza == '2'):
            acumulador += 12
            continue
        elif (adicional_limpeza == '3'):
            acumulador += 20
            continue
        elif (adicional_limpeza == '0'):
            print('****************************************************************************')
            return acumulador
        else:
            print('!!! Opção Inválida !!!')

#----------fim da função adicional limpeza--------


#----------começo do progama principal-------------------------
print('Bem-vindo ao Progama de Serviços de Limpeza do Lucas Rodrigues de Oliveira')
print('****************************************************************************')
metragem_m = (metragem_limpeza())
tipo_l = float(tipo_limpeza())
adicional_l = float(adicional_limpeza())
total = (metragem_m * tipo_l) + adicional_l
print('TOTAL: R${:.2f} (metragem: {:.2f} * tipo: {:.2f} + adicional: {:.2f}) '.format(total,metragem_m, tipo_l, adicional_l))
print('****************************************************************************')
#----------fim do progama principal----------------------------