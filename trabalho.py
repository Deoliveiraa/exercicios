print('Vamos calucalr a media das suas avaliações !!! ')
a = float(input('Me diga qual é a nota que vc tirou ? '))
b = float(input('Qual é a porcentagem que ela vale, ( SEM O SIMBOLO DA PORCENTAGEM % ) '))
c = int(input('Você tem mais alguma nota, digite 1 para sim e 2 para não ? '))
p = b / 100
r = a * p
if  c == 1:
    seg = float(input('Qual o valor da outra nota ? '))
    ter = float(input('Qual é a porcentagem que ela vale, ( SEM O SIMBOLO DA PORCENTAGEM % ) '))
    qua = int(input('Você tem mais alguma nota, digite 1 para sim e 2 para não ? '))
    porcent_dois = ter / 100
    result_dois = seg * porcent_dois
    s = r + result_dois
    if qua == 1:
        outra = float(input('Qual o valor da outra nota ? '))
        outra_p = float(input('Qual é a porcentagem que ela vale, ( SEM O SIMBOLO DA PORCENTAGEM % ) '))
        outra_qua = int(input('Você tem mais alguma nota, digite 1 para sim e 2 para não ? '))
        divi = outra_p / 100
        result_tres = outra * divi
        soma_ultima = result_tres + s
        if outra_qua == 1:
            ultima = float(input('Qual o valor da outra nota ? '))
            ultima_p = float(input('Qual é a porcentagem que ela vale, ( SEM O SIMBOLO DA PORCENTAGEM % ) '))
            divi_ultim = ultima_p / 100
            resultad_f = ultima * divi_ultim
            soma_final = soma_ultima + resultad_f
            print("A sua media é {}".format(soma_final))
        else:
            print(f"A sua media é {soma_ultima}")
    else:
        print('A sua media é {}'.format(s))

else:
    print('A sua media é {}'.format(r))