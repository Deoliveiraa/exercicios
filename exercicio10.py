# escolhendo um produto e calculando os valores 

from cgi import print_form


print("Escolha o produto que deseja a seguir ")
print("Para maça digite numero: 1 ")
print("Para banana digite numero: 2 ")
print("Para laranja digite numero: 3 ")

produto = int(input("Qual é o numero do produto que deseja? "))
quantidade = int(input("Qual a quantidade de produtos que deseja? "))

if (produto == 1):
    preco = quantidade * 2.6
    print("Você comprou {} maças e o valor a pagar é R${} ".format(quantidade,preco))
elif (produto == 2):
    preco = quantidade * 1.85
    print("Você comprou {} banana e o valor a pagar é R${} ".format(quantidade,preco))
elif (produto == 3):
    preco = quantidade * 3.6
    print("Você comprou {} laranja e o valor a pagar é R${} ".format(quantidade,preco))
else:
    print("Erro, por favor refazer o processo produto inexistente ")