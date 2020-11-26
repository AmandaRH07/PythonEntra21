def limpar_tela():
    from os import system, name 
    # for windows 
    if name == 'nt':
        system('cls')
    # for mac and linux(here, os.name is 'posix') 
    else: 
        system('clear')
        
        
def cabecalho(texto="")-> None:
    """
    Esta função retorna uma linha caso não seja dado um parâmetro e
    retorna um texto com uma linha supoerior e outra inferior caso haja uma
    entrada de parâmetro.
    
    Atributo opcional utilizado:
    
    texto: Imprimi um texto formatado para o cabeçalho com max de 50 caracteres
    
    Ex: =======
          Ola
        =======
    """
    print(f"{'':=^50}")

    if texto:
        print(f"{texto.title():^50}")
        print(f"{'':=^50}\n")


def texto_menu(texto: str)-> None:
    print(f"{'':^10}{texto:<40}")


def rodape():
    print(f"\n{'':-^50}")
    

def linha_tabela():
    print(f"{'':-^50}")

# 
# def menu_tabela(texto1, texto2, texto3, texto4, texto5):
    
#     print(f": {texto1:<9}: {texto2:<7}: {texto3:<7}: {texto4:<7}: {texto5:<9}:")


def menu_tabela(*textos):
    for posicao, linha in enumerate(textos):
        print(f"{'':^10}[{posicao+1}] {linha:<40}")
    print(f"\n{'':-^50}")