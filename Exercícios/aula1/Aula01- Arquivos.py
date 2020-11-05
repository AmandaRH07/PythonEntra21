# Arquivos

#== Ler Arquivo
try:
    file = open("arquivo.txt")
    print(file.read())
except:
    print("Erro na leitura do arquivo :(")


#== Escrever no arquivo
try: 
    file = open("arquivo_dois.txt", "w+")
    file.write("Amanda Rafaela Hass;18;Sem animais de estimacao;")
    file.close()
except:
    print("Deu errado :(")

arquivo2 = open("arquivo_dois.txt", "r")
for linha in arquivo2:
    dados =  linha.split(";")
    print(dados[1])