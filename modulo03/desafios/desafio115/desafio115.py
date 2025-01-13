from time import sleep

arq = 'cursoemvideo.txt'

def arquivo_existe(nome):
    try:
        a = open(nome, 'rt') #rt lê o arquivo
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criar_arquivo(nome):
    try:
        a = open(nome, 'wt+') #wt escreve + cria o arquivo
        a.close()
    except:
        print("Houve um ERRO na criação do arquivo!")
    else:
        print(f"Arquivo {nome} criado com sucesso!")
     
# if arquivo_existe(arq):
#     print("Arquivo encontrado com sucesso!")
# else: 
#     print("Arquivo não encontrado!")
#     criar_arquivo(arq)

if not arquivo_existe(arq):
    criar_arquivo(arq)
    
def ler_arquivo(nome):
    try:
        a = open(nome, "rt")
    except:
        print(f"ERRO ao ler o arquivo {nome}!")
    else:
        cabecalho("PESSOAS CADASTRADAS")
        for linha in a:
            dado = linha.split(";") #split divide dados
            dado[1] = dado[1].replace('\n', '')
            print(f"{dado[0]:<30}{dado[1]:>3} anos")
        #print(a.read()) #pega as linha do arquivo e joga em uma lista
    finally:
        a.close()
        
def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, "at") #at append
    except:
        print("Houve um ERRO na abertura do arquivo!")
    else:
        try:
            a.write(f"{nome};{idade}\n")
        except:
            print("Houve um ERRO na hora de escrever os dados!")
        else:
            print(f"Novo registro de {nome} adicionado.")
            a.close() 
 
def leia_int(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO: por favor, digite um número inteiro válido.\033[m")
            continue
        except (KeyboardInterrupt, SystemExit):
            print("\033[31mEntrada de dados interrompida pelo usuário.\033[m")
            return 0 
        else:
            return n

def linha(tam=42):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())
    
def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f"{c} - {item}")
        c += 1
    print(linha())
    opc = leia_int("Sua opção: ")
    return opc
        
while True:
    resposta = menu(["Ver pessoas cadastradas","Cadastrar nova Pessoa","Sair do Sistema"])
    if resposta == 1:
        ler_arquivo(arq)        
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input("Nome: "))
        idade = leia_int("Idade: ")
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print("\033[31mERRO! Digite uma opção válida!\033[m")
    sleep(1)