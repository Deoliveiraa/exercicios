print(' Jogo de adivinhaçãos e numeros')
palpite = 1
numero = 22

while bool(palpite) is True:
    palpite = int(input('Qual é o numero ? '))
    if palpite == numero:
        print('Parabens você acertou !!! ')
        break
    else:
        print('Você errou, tento novamente ')

else:
    print('Erro')