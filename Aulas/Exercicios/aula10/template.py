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

    for pos, texto in enumerate(textos):
        if pos == 0:
            print(f" {texto:<10}",end=" ")
            
        elif pos == len(textos) - 1:
            if pos < 4:
                print(f": {texto:<6}",end=" ")
                print(f": {'':<8}:",end=" ")
            
            else:
                print(f": {texto:<8}:",end=" ")
            
        else:
            print(f": {texto:<6}",end=" ")
    
    print()