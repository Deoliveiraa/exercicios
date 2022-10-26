print("Bem-vindo á loja do Lucas Rodrigues de Oliveira")
valor = float(input("Entre com o valor do produto: "))
quantidade = int(input("Entre com o valor da quantidade: "))
res = valor * quantidade
if (0 <= quantidade < 11):
    valorfinal = res + 30.00
    print("O valor sem frete foi de: R${:.2f} ".format(res))
    print("O valor com frete foi: R${:.2f}   (frete de R$ 30.00)     ".format(valorfinal))
elif (11 <= quantidade < 101):
    valorfinal = res + 60.00
    print("O valor sem frete foi de: R${:.2f} ".format(res))
    print("O valor com frete foi: R${:.2f}   (frete de R$ 60.00)     ".format(valorfinal))
elif (101 <= quantidade < 1001 ):
    valorfinal = res + 120.00
    print("O valor sem frete foi de: R${:.2f} ".format(res))
    print("O valor com frete foi: R${:.2f}   (frete de R$ 120.00)     ".format(valorfinal))
elif (quantidade >= 1001 ):
    valorfinal = res + 240.00
    print("O valor sem frete foi de: R${:.2f} ".format(res))
    print("O valor com frete foi: R${:.2f}   (frete de R$ 240.00)     ".format(valorfinal))
else:
    print("Erro, favor refazer o procecesso") # decidi colocar o Else para um escape de erro