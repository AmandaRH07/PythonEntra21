# Construa uma classe chamada veículo com no minímo 5 atributos e 3 metódos
# Faça outras 3 classes que herdem da classe veículo; por exemplo Carro; e ajuste as funções onde necessário (polimorfismo)
from Pessoas import Pessoa, NovaPessoa
from Veiculos import Veiculo, Carro, Moto, Bicicleta, passageiros, teste

menu = False
opcao = ""

carro = Carro("Chevrolett")
print(carro.ocupacao())

moto = Moto("2")
print(moto.buzina())

bicicleta = Bicicleta("Branco")

veiculos = [carro, moto, bicicleta]

for veiculo in veiculos:
    print(f"""Tipo de veículo: {type(veiculo).__name__}
    Fabricante: {veiculo.fabricante}
    Quantidad de rodas: {veiculo.qtd_rodas}
    Tipo de Combustivel: {veiculo.combustivel}
    Quantidade de lugares: {veiculo.qtd_lugares}
    Cor: {veiculo.cor}\n""")


pessoa1 = NovaPessoa("Amanda","18", "123.456.789-00")
pessoa2 = NovaPessoa("Luana","19", "987.654.321-00")

pessoas = [pessoa1,pessoa2]

for pessoa in pessoas:
    print(f"{pessoa.nome}, {pessoa.idade} anos, CPF: {pessoa.cpf}")
    passageiros.append(pessoa.nome)
    #passageiros.append(pessoa.idade)
    #passageiros.append(pessoa.cpf)

menu = False

def opcoes():
    global opcao
    global menu 
    menu = True
    opcao= input("""\nMENU
    1. Adicionar passageiro
    2. Remover passageiro 
    3. Listar passageiro
    4. Sair
    Insira a opção desejada: """) 

opcoes()

while menu == True:
    if opcao == "1":
        nome = input("Insira o nome: ")
        idade = input("Insira a idade: ")
        cpf = input("Insira o cpf: ")
        carro.addPassageiro(nome)
        pessoas.append(carro)
        passageiros.append(nome)
        #passageiros.append(idade)
        #passageiros.append(cpf)
        menu = teste
        opcoes()
    elif opcao == "2":
        carro.removePassageiro()
        menu = teste
        opcoes()
    elif opcao == "3":
        carro.listarPassageiros()
        menu = teste
        opcoes()
    elif opcao == "4":
        break
    else:
        opcoes()