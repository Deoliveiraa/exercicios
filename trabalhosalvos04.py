from multiprocessing.sharedctypes import Value
from operator import indexOf
import random


lista_funcionario = []
#---------- começo cadastro funcionario -----------
def cadastrar_funcionario(id):
    print('------------------------------- MENU CADASTRAR FUNCIONÁRIO -------------------------------')
    id = random.randint(1,1000)
    print('Código do Funcionário {}'.format(id))
    nome = input('Por favor entre com o NOME: ')
    setor = input('Por favor entre com o SETOR: ')
    salario = float(input('Por favor entre com o SALÁRIO (R$): '))
    print('*' * 90)
    dicionario_funcionario = {'id' : id,
                              'nome' : nome,
                              'setor' : setor,
                              'salario' : salario}
    lista_funcionario.append(dicionario_funcionario.copy())
# fim 


#começo consultar estudantes 
def consultar_funcionario():
    print('------------------------------- MENU CONSULTAR FUNCIONÁRIO -------------------------------')
    while True:
        try:
            opcao_consultar = int(input('Escolha a opção desejada: \n'
                            '1 - Consultar todos os Funcionários \n'
                            '2 - Consultar Funcionários por ID \n'
                            '3 - Consultar Funcionários por SETOR \n'
                            '4 - Retornar \n >>> '))
            if opcao_consultar == 1:
                print('-' * 50)
                for funcionarios in lista_funcionario:
                    for key, Value in funcionarios.items():
                        print('{} : {}'.format(key,Value))
            elif opcao_consultar == 2:
                print('-' * 50)
                entrada = int(input('Digite o ID do Funcionário: '))
                for funcionarios in lista_funcionario:
                    if (funcionarios ['id'] == entrada):
                        for key, Value in funcionarios.items():
                         print('{} : {}'.format(key,Value))
            elif opcao_consultar == 3:
                print('-' * 50)
                entrada = input('Digite o SETOR do Funcionário: ')
                for funcionarios in lista_funcionario:
                    if (funcionarios ['setor'] == entrada):
                        for key, Value in funcionarios.items():
                         print('{} : {}'.format(key,Value))
            elif opcao_consultar == 4:                              
                return
            else:
                print('invalido, refaça o processo ')
                continue
        except ValueError:
             print('Apenas numeros inteiros')
             continue
# fim

#começo consultar estudantes 
def remover_funcionario():                                                                
    print('------------------------------- MENU REMOVER FUNCIONÁRIO ---------------------------------')
    entrada = int(input('Digite o ID do Funcionário: '))
    for funcionarios in lista_funcionario:
        if (funcionarios ['id'] == entrada):
            lista_funcionario.remove(funcionarios)
            print('*' * 90)
            return
#fim


# MAIN
print('Bem-Vindo ao controle de Funcionários do Lucas Rodrigues de Oliveira')
print('*' * 90)
registro_id = 0
while True:
    print('------------------------------- MENU PRINCIPAL -------------------------------------------')
    try:
        opcao = int(input('Escolha a opção desejada: \n'
                        '1 - Cadastrar Funcionário \n'
                        '2 - Consultar Funcionário(s) \n'
                        '3 - Remover Funcionario \n'
                        '4 - Sair \n >>> '))
        print('*' * 90)
        if opcao == 1:
            registro_id += 1
            cadastrar_funcionario(id)
        elif opcao == 2:
            consultar_funcionario()
        elif opcao == 3:
            remover_funcionario()
        elif opcao == 4:                              
            print('Finalizando Progama')
            break
        else:
            print('Opção inválida, tente novamente ')
            continue
    except ValueError:
        print('Apenas numeros inteiros')
        continue
