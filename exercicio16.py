from random import betavariate


cadastro = {'nome':[], 'sexo':[], 'ano':[]}

while True:
   terminar = input('Deseja cadastrar uma pessoa? [S/N}')
   if terminar.upper() in 'N':
    break
   elif terminar.upper() not in 'S':
    print('Digite S para SIM ou N para NÃO') 
    continue

   nome = input('Qual seu nome?')
   sexo = input('Qual seu sexo [M/F]?')
   ano = int(input('Qual seu nascimento?'))
   cadastro['nome'].append(nome)
   cadastro['sexo'].append(sexo.upper())
   cadastro['ano'].append(ano)

print(cadastro)    