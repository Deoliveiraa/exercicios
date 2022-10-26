print('CALCULADORA')
print('+ adição')
print('- subtração')
print('* multiplicação')
print('/ divisão')
print('escreva sair para encerrar')

op = input('Qual operação deseja fazer? ')
if op == '+' or op == '-' or op == '*' or op == '/':
    x = int(input('Digite o primeiro valor: '))
    y = int(input('Digite o segundo valor: '))

while (op != 'sair'):
    if (op == '+'):
        res = x + y
        print('Resultado: {} + {} = {}'.format(x,y,res))
    elif (op == '-'):
        res = x - y 
        print('Resultado: {} - {} = {}'.format(x,y,res))
    elif (op == '*'):
        res = x * y
        print('Resultado: {} x {} = {}'.format(x,y,res)) 
    elif (op == '/'):
        res = x / y
        print('Resultado: {} / {} = {}'.format(x,y,res))     
    else:
        print('Operação invalida')    
    op = input('Qual operação deseja fazer? ')
    if op == '+' or op == '-' or op == '*' or op == '/':
        x = int(input('Digite o primeiro valor: '))
        y = int(input('Digite o segundo valor: '))
print('Progama Encerrado')        