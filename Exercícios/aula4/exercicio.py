# Construa uma classe chamada veículo com no minímo 5 atributos e 3 metódos
# Faça outras 3 classes que herdem da classe veículo; por exemplo Carro; e ajuste as funções onde necessário (polimorfismo)
from Pessoas import Pessoa, Pessoa1, Pessoa2
from Veiculos import Veiculo, Carro, Moto, Bicicleta, passageiros

menu = False

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

pessoa1 = Pessoa1("18")
pessoa2 = Pessoa2("19")

pessoas = [pessoa1,pessoa2]

for pessoa in pessoas:
    print(f"{pessoa.nome}, {pessoa.idade} anos, CPF: {pessoa.cpf}")
    passageiros.append(pessoa)

menu = True
opcao = input("""\nMENU
    1. Adicionar passageiro
    2. Remover passageiro 
    3. Listar passageiro
    Insira a opção desejada: """) 

while menu == True:
    if opcao == "1":
        carro.addPassageiro()
        pessoas.append(carro)
    elif opcao == "2":
        carro.removePassageiro()
    elif opcao == "3":
        carro.listarPassageiros()
    else:
        break