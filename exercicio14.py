# Lista de jogos e videogames 

def valida_int(pergunta, min , max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def criaArquivo(nomearquivo):
    try:
         a = open(nomearquivo, 'wt+')
         a.close()
    except:
        print('Erro ana criação do arquivo')
    else: 
        print('Arquivo {} foi criado com sucesso!\n'.format(nomearquivo))        

def existearquivo(nomearquivo):
    try:
        a = open(nomearquivo,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True     

def cadastrarjogo(nomearquivo, nomejogo, nomevideogame):
    try:
        a = open(nomearquivo, 'at')
    except:
        print('Erro ao abrir o arquivo')
    else:
        a.write('{};{}\n'.format(nomejogo,nomedovideogame))     
    finally:
        a.close()

def listararquivo(nomearquivo):
    try:
        a = open(nomearquivo , 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        print(a.read())   
    finally:
        a.close() 

# progama principal 
arquivo = 'games.txt'
if existearquivo(arquivo):
    print('Arquivo localizado no computador ')
else:
    print('Arquivo inexistente ')    
    criaArquivo(arquivo)

while True:
    print('MENU') 
    print('1 - Cadastrar novo item')
    print('2 - Listar Cadastro')
    print('3 - Sair')

    op = valida_int('Escolha a opção desejada: ' , 1, 3)
    if op == 1:
        print('Opção de cadastrar novo item selecionada ...\n')
        nomejogo = input('Nome do jogo: ')
        nomedovideogame = input('Nome do Video Game: ')
        cadastrarjogo(arquivo, nomejogo, nomedovideogame)

    elif op == 2:
        print('Opção de listar selecionada...\n')
        listararquivo(arquivo)

    elif op == 3:
        print('Encerrando programa ...')  
        break 
