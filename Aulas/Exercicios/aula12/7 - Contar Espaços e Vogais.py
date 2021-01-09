"""
Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte
    quantos espaços em branco existem na frase.
    quantas vezes aparecem as vogais a, e, i, o, u. 

"""
import exercises as cabecalho

cabecalho.cabecalho("conta espaços e vogais")

def conta_frase(frase = ""):
    
    print(f"""
    O espaço aparece {frase.count(" ")} vezes.
    A vogal A parece {frase.count("a")} vezes
    A vogal E parece {frase.count("e")} vezes
    A vogal I parece {frase.count("i")} vezes
    A vogal O parece {frase.count("o")} vezes
    A vogal U parece {frase.count("u")} vezes
    """)
    return False

if __name__ == "__main__":

    while True:
        opcao = int(input("\nPara inserir uma frase digite 1: "))

        if opcao == 1:
            frase = input("\nInsira a frase: ")
            conta_frase(frase)
        else:
            break

# Forma anterior
    #tamanho_string = len(frase.lower())

    # contador_espaco = 0
    # contador_a = 0
    # contador_e = 0
    # contador_i = 0
    # contador_o = 0
    # contador_u = 0
# 
    # for caractere in frase:
        # if caractere == " ":
            # contador_espaco += 1
        
        # if caractere == "a":
            # contador_a += 1
         
        # if caractere == "e":
            # contador_e += 1
         
        # if caractere == "i":
            # contador_i += 1

        # if caractere == "o":
            # contador_o +=1

        # if caractere == "u":
            # contador_u += 1
        
