from os import system, name 

palavra = ""
chances = 0

def carregar_config():
    global palavra
    global chances
    linhas_arquivo = []
    with open("forca.cfg") as f:
        for linha in f:
            linhas_arquivo.append(linha.strip())
    palavra = str(linhas_arquivo[0])
    chances = int(linhas_arquivo[1])

def jogar():
    global palavra
    global chances
    carregar_config()
    letras_usadas = []
    
    opcoes = int(input(f"""
    MENU
    1 - Jogar
    2 - Modificar as configurações
    3 - Sair
    Insira a opção desejada: """))

    while True:
        if opcoes == 1:
            tentativa_palavra = ""
            #global tentativa_palavra
            numeros = ["0","1","2","3","4","5","6","7","8","9"]
            limpa_tela()  
    
            print("Número de chances: %d - tentativas:" % chances) # interpolação de string
            print(*letras_usadas) # imprime item por item do array
            print("\n")
            for x in palavra:
                tentativa_palavra += x if x in letras_usadas else "_"
            print(tentativa_palavra + "\n\n")
        
            chute = input("Digite uma letra: ")      
            if chute in letras_usadas:
                chute = input("Letra repetida! Digite outra letra: ")
                letras_usadas.append(chute)
            else: 
                letras_usadas.append(chute)
                for i in chute:
                    for j in numeros:
                        if i == j:
                            chute = input("Você digitou um número! Digite uma letra: ")
                            letras_usadas.append(chute)
                
            if not chute in palavra:
                chances -= 1
                
            if chances == 0:
                print("Você perdeu!")
                break
        
            verifica_fim_jogo()

            if tentativa_palavra == palavra:
                #print("Você ganhou com apenas %d!" % 5 - chances)
                print(f"Você ganhou com apenas {chances} chance(s)!")
                break
        elif opcoes == 2:
            modConfig()
        elif opcoes == 3:
            print("Você escolheu sair ")
            break

def verifica_fim_jogo():
    if tentativa_palavra == palavra:
        print(f"Você ganhou com apenas {chances} chance(s)!")
        pass

def limpa_tela():
    # for windows 
    if name == 'nt': 
            system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        system('clear')

def modConfig():
    arquivo = open("forca.cfg", "w+")
    nova_palavra = input("Insira a nova palavra: ")
    nova_chance = input("Insira a nova quantidade de chances: ")
    arquivo.write(f"{nova_palavra}\n{nova_chance}")
    arquivo.close()

if __name__ == "__main__":
    jogar()

    # implementar a função carregar_config ok
    # implementar a função verifica_fim_jogo
    # implementar a função limpar_tela ok

    # previnir que o usuário digite números ok
    # previnir que o usuário repita letras

    # implementar menu de usuário com as seguintes opções:
    # 1 - Jogar ok
    # 2 - Modificar as configurações
    # 3 - sair ok
    
    # https://realpython.com/quizzes/python-dicts/viewer/