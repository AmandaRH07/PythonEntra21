import sqlite3
from veiculos import Pessoa, Veiculo
import template as template2

def cadastrar_no_banco():
    """
    Essa função é responsável pelo cadastro no banco de dados, o usuário 
    pode escolher cadastrar uma pessoa ou um veículo.
    
    """
    template2.cabecalho("Cadastro")
    template2.texto_menu("[1] Pessoa")
    template2.texto_menu("[2] Veículo")
    template2.rodape()
    
    while True:
        try:
            resp = int(input("Selecione uma opção:\n"))

            if resp not in range(1,3):
                print("Você digitou uma opção inválida. Tente novamente!")
                continue
            
            else:
                break
        
        except:
            print("Você digitou uma opção inválida. Tente novamente!")
            continue
        
    conn = sqlite3.connect("Cadastro_Geral.db")
    cursor = conn.cursor()
    
    if resp == 1:
        
        nome = input("Nome:\n")
        data_nascimento = input("Data de nascimento:\n")
        cpf = input("CPF:\n")
        endereco = input("Endereço:\n")
        salario = float(input("Salário:\n"))
        profissao = input("Profissão:\n")
        telefone = input("Telefone:\n")
        nome_responsavel = input("Nome do Responsável:\n")
        sexo = input("Sexo:\n")
        naturalidade = input("Naturalidade:\n")
        nacionalidade = input("Nacionalidade:\n")
        
        pessoa = Pessoa(nome, data_nascimento, cpf, endereco, salario,
                        profissao, telefone, nome_responsavel, sexo,
                        naturalidade, nacionalidade)
        
        
        cadastro_pessoa = (pessoa.nome, pessoa.data_nascimento, pessoa.cpf, pessoa.endereco,
             pessoa.salario, pessoa.profissao, pessoa.telefone,
             pessoa.nome_responsavel, pessoa.sexo, pessoa.naturalidade,
             pessoa.nacionalidade, 0)
        
        try:
            cursor.execute("""
                INSERT INTO Cadastro_pessoa(nome, data_nascimento, cpf, endereco,
                salario, profissao, telefone, nome_responsavel, sexo,
                naturalidade, nacionalidade, veiculo_id)
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?) 
                """, cadastro_pessoa)
            
        except Exception as ex:
            conn.rollback()
            msg = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = msg.format(type(ex).__name__, ex.args)
            print(message)
            
        conn.commit()
        
    if resp == 2:
        
        marca = input("Marca:\n")
        nome = input("Nome do carro:\n")
        modelo = input("Modelo:\n")
        placa = input("Placa:\n")
        proprietario = input("Proprietário:\n")
        cor = input("Cor:\n")
        km_rodado = input("Kilometros rodados:\n")
        qte_passageiros = input("Quantidade de lugares:\n")
        motor = input("Motor:\n")
        combustivel = input("Combustível:\n")
        meio_locomocao = input("Meio de locomoção:\n")
        valor = input("Valor:\n")
        
        carro = Veiculo(marca, nome, modelo, placa, proprietario, cor,
                        km_rodado, qte_passageiros, motor, combustivel,
                        meio_locomocao, valor)
        
        cadastro_veiculo = (carro.marca, carro.nome, carro.modelo, carro.placa,
            carro.proprietario, carro.cor, carro.km_rodado,
            carro.qte_passageiros, carro.motor, carro.combustivel,
            carro.meio_locomocao, carro.valor)
        
        try:
            cursor.execute("""
                INSERT INTO Cadastro_veiculo(marca, nome, modelo, placa,
                proprietario, cor, km_rodado, qte_passageiros, motor,
                combustivel, meio_locomocao, valor)
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?) 
                """, cadastro_veiculo)

            conn.commit()
            
            print("Cadastro efetuado com sucesso!")

        except Exception as ex:
            conn.rollback()
            msg = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = msg.format(type(ex).__name__, ex.args)
            print(message)
    
        
    # cursor.execute("""
    #     SELECT * FROM Cadastro_pessoa INNER JOIN Cadastro_veiculo ON Cadastro_pessoa.veiculo_id = Cadastro_veiculo.id
    #     """)
    
    # print(cursor.fetchall())
    
    conn.close()


def criar_tabelas(): 
    """
    Função que cria a tabelas adiciona as colunas, de acordo com a função da tabela.
    
    """
    conn = sqlite3.connect("Cadastro_Geral.db")
    cursor = conn.cursor()

    try:
        cursor.executescript("""
            CREATE TABLE Cadastro_veiculo(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                marca TEXT NOT NULL,
                nome TEXT NOT NULL,
                modelo TEXT NOT NULL,
                placa TEXT NOT NULL,
                proprietario TEXT NOT NULL,
                cor TEXT NOT NULL,
                km_rodado INTEGER,
                qte_passageiros INTEGER,
                motor INTEGER NOT NULL,
                combustivel TEXT NOT NULL,
                meio_locomocao TEXT NOT NULL,
                valor REAL NOT NULL
            );
            
            CREATE TABLE Cadastro_pessoa(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                data_nascimento TEXT NOT NULL,
                cpf VARCHAR(11) NOT NULL,
                endereco TEXT NOT NULL,
                salario REAL,
                profissao TEXT NOT NULL,
                telefone VARCHAR(11),
                nome_responsavel TEXT NOT NULL,
                sexo TEXT NOT NULL,
                naturalidade TEXT NOT NULL,
                nacionalidade TEXT NOT NULL,
                veiculo_id INTEGER,
                
                FOREIGN KEY (veiculo_id) REFERENCES Cadastro_veiculo(id)
            );
            """)

        print("Tabela criada com sucesso!")
        
    except Exception as ex:
        msg = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = msg.format(type(ex).__name__, ex.args)
        print(message)
        print("Tabela já criada neste banco de dados! Para alterações, "
            "use o UPDATE!")
    
    conn.close()


def deletar_no_banco():
    """
    Essa função é responsável por deletar uma pessoa ou veículo no banco de 
    dados.
    
    """
    template2.cabecalho("Deletar Cadastro")
    template2.texto_menu("[1] Pessoa")
    template2.texto_menu("[2] Veículo")
    template2.rodape()
    
    while True:
        try:
            resp = int(input("Selecione uma opção:\n"))

            if resp not in range(1,3):
                print("Você digitou uma opção inválida. Tente novamente!")
                continue
            
            else:
                break
        
        except:
            print("Você digitou uma opção inválida. Tente novamente!")
            continue
      
    conn = sqlite3.connect('Cadastro_Geral.db')
    cursor = conn.cursor()

    
    if resp == 1:
        
        #Adicionar funcao para mostrar ID's e nome para deletar
    
        id_cliente = int(input("Qual id de pessoa você gostaria de deletar?"))
        
    try:
        # excluindo um registro da tabela
        cursor.execute("""
        DELETE FROM Cadastro_pessoa
        WHERE id = ?
        """, (id_cliente,))

        conn.commit()

        print('Registro excluido com sucesso.')
    
    except Exception as ex:
        conn.rollback()
        msg = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = msg.format(type(ex).__name__, ex.args)
        print(message)

    if resp == 2:
        
        #Adicionar funcao para mostrar ID's e nome para deletar
    
        id_cliente = int(input("Qual id de pessoa você gostaria de deletar?"))
        
    try:

        # excluindo um registro da tabela
        cursor.execute("""
        DELETE FROM Cadastro_veiculo
        WHERE id = ?
        """, (id_cliente,))

        conn.commit()

        print('Registros excluidos com sucesso.')
    
    except Exception as ex:
        conn.rollback()
        msg = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = msg.format(type(ex).__name__, ex.args)
        print(message)

    conn.close()


def update():
    """
    Função usada para o usuário atualizar uma informação no banco de dados.
    
    """
    conn = sqlite3.connect('Cadastro_Geral.db')
    cursor = conn.cursor()

    escolha = int(input("Você gostaria de atualizar?\n\n[1] Pessoa\n\n"
                        "[2] Veículo\n\n[3] Vincular veículo a uma pessoa\n\n"))
    
    if escolha == 1:
        lista = cursor.execute("""PRAGMA table_info(Cadastro_pessoa)""")
        print("Você optou por alterar cadastro em uma pessoa.\n")
        
    elif escolha == 2:
        lista = cursor.execute("""PRAGMA table_info(Cadastro_veiculo)""")
        print("Você optou por alterar cadastro em um veículo.\n")
    
    elif escolha == 3:
        apresentar_banco("pessoas_sem_veiculo")
        id_cliente = int(input("À quem você gostaria de "
                              "vincular um veículo?\nID: "))
        
        apresentar_banco("Veiculos_sem_pessoas")
        
        
        id_veiculo = int(input("Qual veículo você gostaria de vincularw\nID: "))
        
        cursor.execute(f"""
            UPDATE Cadastro_pessoa
            SET veiculo_id = '{id_veiculo}'
            WHERE id = {id_cliente}
            """)
    
    if escolha == 1 or escolha == 2:        
        opcoes = []
        
        for opcao in lista:
            opcoes.append(opcao[1])

        for num, opcao in enumerate(opcoes):
            if num != 0:
                print(f"[{num}] - {opcao}")
        
        opc = int(input("\nInsira uma opção para atualizar:\n"))
        
        campo_atualizar = opcoes[opc]
        
        id_cliente = int(input("\nInsira o id que você deseja alterar:\n"))
        
        atualizacao = input(f"\nInsira a nova informação para atualizar o campo "
                            f"{campo_atualizar}:\n")
        
    # alterando os dados da tabela
    if escolha == 1:
        cursor.execute(f"""
        UPDATE Cadastro_pessoa
        SET {campo_atualizar} = '{atualizacao}'
        WHERE id = {id_cliente}
        """)
    
    elif escolha == 2:
        cursor.execute(f"""
        UPDATE Cadastro_veiculo
        SET {campo_atualizar} = '{atualizacao}'
        WHERE id = {id_cliente}
        """)

    conn.commit()
    
    conn.close()
    
    
def apresentar_banco(entrada = "tudo"): 
    """
    Essa função é responsável por mostrar os dados escolhidos, o usuário 
    pode escolher mostrar uma pessoa que ainda não está vinculada a um 
    veículo, um veículo que ainda não está vinculado a uma pessoa ou uma
    pessoa com veículo.    
    """
    conn = sqlite3.connect('Cadastro_Geral.db')
    cursor = conn.cursor()
    
    if entrada == "pessoas_sem_veiculo":
        cursor.execute("""
            SELECT id, nome FROM Cadastro_pessoa
            Where veiculo_id = 0
            """)
        
        tabela_nomes = cursor.fetchall()
        
        for linha in tabela_nomes:
            print(f"\nID:{linha[0]}\nNome:{linha[1]}\n")
    
        conn.close()
        

    if entrada == "Veiculos_sem_pessoas":
        cursor.execute("""
            SELECT id, nome, placa FROM Cadastro_veiculo;
            """)
        lista_veiculos = cursor.fetchall()
        
       # Primeiro seleciona os veículos que estão ligados a pessoa
       # para depois tirar da lista de pessoas com veículo, sobrando 
       # as sem veículo         
        cursor.execute("""
                SELECT veiculo_id FROM Cadastro_pessoa
                Where veiculo_id != 0
                """)
        
        lista_pessoas_com_veiculos = cursor.fetchall()
        
        for carro in lista_veiculos:
            if not carro[0] in lista_pessoas_com_veiculos:
                print(f"\nID: {carro[0]}\n"
                      f"Veículo: {carro[1]}\n"
                      f"Placa: {carro[2]}\n\n")
        
        conn.close()
        
    if entrada == "tudo":
        template2.cabecalho("Tabela de Cadastros")
        template2.texto_menu("[1] Pessoa")
        template2.texto_menu("[2] Veículo")
        template2.texto_menu("[3] Pessoas veículo")
        # template2.texto_menu("[4] Pessoas sem veículo")
        
        template2.rodape()
        
        while True:
            try:
                resp = int(input("Selecione uma opção:\n"))

                if resp not in range(1,4):
                    print("Você digitou uma opção inválida. Tente novamente!")
                    continue
                
                else:
                    break
            
            except:
                print("Você digitou uma opção inválida. Tente novamente!")
                continue
    
        if resp == 1:
            cursor.execute("""
                    SELECT id, nome FROM Cadastro_pessoa;
                    """)
            
            tabela_nomes = cursor.fetchall()
            
            for linha in tabela_nomes:
                print(f"\nID:{linha[0]}\nNome:{linha[1]}")

            resp = int(input("\nSelecione o ID para ver o cadastro completo.\nDigite "
                        "0 para sair:\n"))
            
            if resp == 0:
                return None

            else:
                lista = cursor.execute("""PRAGMA table_info(Cadastro_pessoa)""")
                opcoes = []
                # Adiciona o nome da pessoa
                for opcao in lista:
                    opcoes.append(opcao[1])
                opcoes = tuple(opcoes)
                    
                cursor.execute(f"""
                SELECT * FROM Cadastro_pessoa
                WHERE id = {linha[0]}
                """)

                matriz = [opcoes]

                matriz.append(cursor.fetchone())

                # Para printar todas as informações do cadastro pessoa 
                for indice in range(len(opcoes)):
                    primeira_coluna = True
                    for linha in matriz:
                        if primeira_coluna:
                            #mostra as informações da coluna da tabela
                            print(f"{linha[indice]:>17}", end = " "*3)
                            primeira_coluna = False
                            
                        else:
                            #mostra as informações do banco de dados do id selecionado
                            print(f"{linha[indice]:<20}", end = " ")

                    print()         
                
                input("\nPressione Enter para continuar.\n")
                
        if resp == 2:
                
            cursor.execute("""
                    SELECT id, nome, placa FROM Cadastro_veiculo;
                    """)
            
            tabela_nomes = cursor.fetchall()
            
            for linha in tabela_nomes:
                print(f"\nID: {linha[0]}\nNome: {linha[1]}\nPlaca: {linha[2]}")
            
            resp = int(input("\nSelecione o ID para ver o cadastro completo.\nDigite "
                        "0 para sair:\n"))
            
            if resp == 0:
                return None

            else:
                lista = cursor.execute("""PRAGMA table_info(Cadastro_veiculo)""")
                opcoes = []
                for opcao in lista:
                    opcoes.append(opcao[1])
                opcoes = tuple(opcoes)
                    
                cursor.execute(f"""
                SELECT * FROM Cadastro_veiculo
                WHERE id = {linha[0]}
                """)

                matriz = [opcoes]
                matriz.append(cursor.fetchone())
                for indice in range(len(opcoes)):
                    primeira_coluna = True
                    for linha in matriz:
                         #mostra as informações da coluna da tabela
                        if primeira_coluna:
                            print(f"{linha[indice]:>17}", end = " "*3)
                            primeira_coluna = False
                            
                        else:
                             #mostra as informações do banco de dados do id selecionado
                            print(f"{linha[indice]:<20}", end = " ")

                    print()         
                
                input("\nPressione Enter para continuar.\n")
                
        if resp == 3:
            
            cursor.execute("""
                SELECT Cadastro_pessoa.id, Cadastro_pessoa.nome, Cadastro_veiculo.nome,
                Cadastro_veiculo.placa
                FROM Cadastro_pessoa INNER JOIN Cadastro_veiculo
                ON Cadastro_pessoa.veiculo_id = Cadastro_veiculo.id
                """)
            
            for linha in cursor.fetchall():
                print(f"\nID: {linha[0]}\nProprietário: {linha[1]}\n"
                    f"Veículo: {linha[2]}\nPlaca: {linha[3]}\n\n")
            
            
            resp = int(input("\nSelecione o ID para ver o cadastro completo."
                             "\nDigite 0 para sair:\n"))
            
            if resp == 0:
                return None

            else:
                lista = cursor.execute("""PRAGMA table_info(Cadastro_pessoa)""")

                opcoes1 = []
                for opcao1 in lista:
                    opcoes1.append(opcao1[1])
                opcoes1 = tuple(opcoes1)
                
                lista2 = cursor.execute("""PRAGMA table_info(Cadastro_veiculo)""")
                
                opcoes2 = []
                for opcao2 in lista2:
                    opcoes2.append(opcao2[1])
                opcoes2 = tuple(opcoes2)
                    
                cursor.execute(f"""
                    SELECT * FROM Cadastro_pessoa
                    WHERE id = {resp}
                    """)

                matriz = [opcoes1]

                matriz.append(cursor.fetchone())
                matriz.append(opcoes2)
                
                cursor.execute(f"""
                    SELECT * FROM Cadastro_veiculo
                    WHERE id = {resp}
                    """)
                
                matriz.append(cursor.fetchone())
                print()
                for indice in range(len(opcoes1)):
                    primeira_coluna = True
                    terceira_coluna = False
                    for linha in matriz:
                        if primeira_coluna:
                            print(f"{linha[indice]:>17}:", end = " "*2)
                            primeira_coluna = False
                            
                        elif not terceira_coluna and not primeira_coluna:   
                            print(f"{linha[indice]:<20}", end = " |")
                            terceira_coluna = True
                        
                        elif terceira_coluna:
                            print(f"{linha[indice]:>17}:", end = " "*2)
                            terceira_coluna = False
                        
                    print()         
                
                input("\nPressione Enter para continuar.\n")