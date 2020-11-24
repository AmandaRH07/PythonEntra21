#marca, nome, modelo, placa, proprietario, cor, km_rodado, qte_passageiros,
#motor, combustivel, meio_locomocao.

from func_banco import *
import template as template
from time import sleep

class Veiculo():
    def __init__(self, marca, nome, modelo, placa, proprietario, cor, km_rodado,
                 qte_passageiros, motor, combustivel, meio_locomocao, valor):
        
        self.marca = marca
        self.nome = nome
        self.modelo = modelo
        self.placa = placa
        self.proprietario = proprietario
        self.cor = cor
        self.km_rodado = km_rodado
        self.qte_passageiros = qte_passageiros
        self.motor = motor
        self.combustivel = combustivel
        self.meio_locomocao = meio_locomocao
        self.valor = valor
        
        
    def __str__(self):
        pass
    
    
class Pessoa():
    def __init__(self, nome, data_nascimento, cpf, endereco, salario, profissao,
                 telefone, nome_responsavel, sexo, naturalidade,
                 nacionalidade):
        
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco
        self.salario = salario
        self.profissao = profissao
        self.telefone = telefone
        self.nome_responsavel = nome_responsavel
        self.sexo = sexo
        self.naturalidade = naturalidade
        self.nacionalidade = nacionalidade  
        
           
    def __str__(self):
        pass    
    
    
def main():
    
    while True:
          
        template.cabecalho("Cadastro Master Blaster Mega do Detran Barril")
        template.texto_menu("[1] Criar Banco de Dados")
        template.texto_menu("[2] Cadastrar")
        template.texto_menu("[3] Atualizar Cadastro")
        template.texto_menu("[4] Mostrar Cadastros")
        template.texto_menu("[5] Deletar Cadastro")
        template.texto_menu("[6] Sair")
        template.rodape()
        
        while True:
            try:
                resp = int(input("Selecione uma opção:\n"))

                if resp not in range(1,7):
                    print("Você digitou uma opção inválida. Tente novamente!")
                    continue
                
                else:
                    break
            
            except:
                print("Você digitou uma opção inválida. Tente novamente!")
                continue
            
        if resp == 1:
            criar_tabelas()
            sleep(1)
            
        elif resp == 2:
            while True:
                cadastrar_no_banco()
                resp = input("Você gostaria de realizar outro "
                             "cadastro? [S/N]\n").lower().strip()[0]
                
                if resp in "sn" and resp != "" and resp != " ":
                    break
                
                else:
                    continue
                
        elif resp == 3:
            update()
        
        elif resp == 4:
            apresentar_banco()
        
        elif resp == 5:  
            while True:
                deletar_no_banco()
                resp = input("Você gostaria de deletar outro "
                             "cadastro? [S/N]\n").lower().strip()[0]
                
                if resp in "sn" and resp != "" and resp != " ":
                    break
                
                else:
                    continue
        
        elif resp == 6:
            print("Obrigado por usar nossos serviços!")
            break
        
        else:
            print("Ops, algo deu errado. Tente novamente!")
            sleep(1)
        
if __name__ == "__main__":
    main()