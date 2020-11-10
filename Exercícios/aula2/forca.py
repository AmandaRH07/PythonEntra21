from os import system, name 

palavra = ""
chances = 0
opcao = 0
letras_usadas = []

def carregar_config():
    global palavra
    global chances
    linhas_arquivo = []
    with open("C:\Python_Entra21\Entra21_Python\Forca.cfg") as f:
        for linha in f:
            linhas_arquivo.append(linha.strip())
    palavra = str(linhas_arquivo[0])
    chances = int(linhas_arquivo[1])

def jogar():
    global palavra
    global chances
    global opcao
    global letras_usada
    carregar_config()
    opcoes()

    while True:
        tentativa_palavra = ""
        if opcao == 1: 
            numeros = ["0","1","2","3","4","5","6","7","8","9"]
            limpa_tela()  
            print("Número de chances: %d - tentativas:" % chances) # interpolação de string
            print(*letras_usadas) # imprime item por item do array
            print("\n")

            for x in palavra:
                tentativa_palavra += x if x in letras_usadas else "_"
            print(tentativa_palavra + "\n\n")

            chute = input("Digite uma letra: ")
            for i in chute:
                for j in numeros:
                    if i == j:
                        chute = input("Você digitou um número! Digite uma letra: ")
                        letras_usadas.append(chute)    
            if chute in letras_usadas:
                chute = input("Letra repetida! Digite outra letra: ")
                letras_usadas.append(chute)
            else: 
                letras_usadas.append(chute)
                        
            if not chute in palavra:
                chances -= 1
                    
            if chances == 0:
                print("Você perdeu!")
                break
            
            verifica_fim_jogo(tentativa_palavra,palavra,letras_usadas)

        if opcao == 2:
            modifica_Config()
            opcoes()
        if opcao == 3:
                print("Você escolheu sair ")
                break
       
def opcoes():
    global opcao
    opcao = int(input(f"""\nMENU \n1 - Jogar\n2 - Modificar as configurações\n3 - Sair\nInsira a opção desejada: """))

def verifica_fim_jogo(tentativa_palavra,palavra,letras_usadas):
    if tentativa_palavra == palavra:
        print(f"Você ganhou com apenas {chances} chance(s)!")
        letras_usadas.clear()
        opcoes()

def limpa_tela():
    # for windows 
    if name == 'nt': 
            system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        system('clear')

def modifica_Config():
    arquivo = open("C:\Python_Entra21\Entra21_Python\Forca.cfg", "w")
    nova_palavra = input("Insira a nova palavra: ")
    nova_chance = input("Insira a nova quantidade de chances: ")
    arquivo.write(f"{nova_palavra}\n{nova_chance}")
    arquivo.close()
    carregar_config()

if __name__ == "__main__":
    jogar()

    # implementar a função carregar_config ok
    # implementar a função verifica_fim_jogo ok
    # implementar a função limpar_tela ok

    # previnir que o usuário digite números ok
    # previnir que o usuário repita letras +/-

    # implementar menu de usuário com as seguintes opções:
    # 1 - Jogar ok
    # 2 - Modificar as configurações ok
    # 3 - sair ok
    
    # https://realpython.com/quizzes/python-dicts/viewer/