# sabendo o valor que ira pagar por Kwh consumido 
print('Preciso que informe qual o tipo de instalação')
print('Digite R para residencial ')
print('Digite I para indústrial ')
print('Digite C para comercial ')
tipo = input("Qual é o tipo de instalação? ")
kw = float(input("Qual é a quantidade de Kwh consumidos? "))
if (tipo == 'R'):
    if (kw <= 500):
        res = kw * 0.40
        print("O seu tipo de instalação é {} e você consumiu {} Kwh ficando assim um valor de R${} para pagar ".format(tipo,kw,res))
    elif (kw > 500):
        res1 = kw * 0.65
        print("O seu tipo de instalação é {} e você consumiu {} Kwh ficando assim um valor de R${} para pagar ".format(tipo,kw,res1))
    else:
        print('Erro, refazer o processo')    
elif (tipo == 'I'):
    if (kw <= 5000):
        res2 = kw * 0.55
        print("O seu tipo de instalação é {} e você consumiu {} Kwh ficando assim um valor de R${} para pagar ".format(tipo,kw,res2)) 
    elif (kw > 5000):
        res3 = kw * 0.60
        print("O seu tipo de instalação é {} e você consumiu {} fkwh icando assim um valor de R${} para pagar ".format(tipo,kw,res3))
    else:
        print("Erro, refazer o processo ")
elif (tipo == 'C'):
    if (kw <= 100):
        res4 = kw * 0.55
        print("O seu tipo de instalação é {} e você consumiu {} Kwh ficando assim um valor de R${} para pagar ".format(tipo,kw,res4))
    elif (kw > 100):
        res5 = kw * 0.60
        print("O seu tipo de instalação é {} e você consumiu {} Kwhficando assim um valor de R${} para pagar ".format(tipo,kw,res5))   
    else:
        print("Erro, refazer o processo ")    
else:
    print("Fora das regras ")    
