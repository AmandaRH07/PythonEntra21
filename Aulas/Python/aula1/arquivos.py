import os

# diretório atual
print(os.getcwd())

# caminho absoluto
print(os.path.abspath('aula_um.py'))

# arquivo/caminho existe
print(os.path.exists('aula_um.py'))

# é um diretório?
print(os.path.isdir('aula_um.py'))

# lista arquivos
print(os.listdir('/home'))

# junta diretórios
print(os.listdir(os.path.join('/home','bruno')))

# ler arquivo
try:
    file = open('arquivo.txt')
    print(file.read())
except:
    print("ops, deu ruim!")


# ler arquivo
try:
    file = open('arquivo_novo.txt', 'w')
    print(file.write("Esse é um novo arquivo!"))
    file.close()
except:
    print("ops, deu ruim!")

# ler arquivo
try:
    with open('arquivo_dois.txt') as f:
        for line in f:
            print(line.strip())
        f.close()
except Exception as e:
    print("ops, deu ruim!")
    print(e)



