# Crie as seguintes classes com suas determinadas carcteristicas
# ram, hd, processador

# Agora, crie a classe Placa_mae, que deve ser composta pelos 3 itens acima

# Por fim, utilizando herança, crie dispositivos que utilizam a placa mãe; 
# por exemplo: computador

class Ram: 
    def __init__(self, leitura_dados_ram, gravacao_dados_ram):
        self.leitura_dados_ram = leitura_dados_ram
        self.gravacao_dados_ram = gravacao_dados_ram

class Hd:
    def __init__(self,leitura_dados_hd, gravacao_dados_hd):
        self.leitura_dados_hd = leitura_dados_hd
        self.gravacao_dados_hd = gravacao_dados_hd

class Processador:
    def __init__(self,core):
        self.core = core

class Placa_mae(Ram, Hd, Processador):
    def __init__(self, leitura_dados_ram, gravacao_dados_ram, leitura_dados_hd, gravacao_dados_hd, core):
        self.leitura_dados_ram = leitura_dados_ram
        self.gravacao_dados_ram = gravacao_dados_ram
        self.leitura_dados_hd = leitura_dados_hd
        self.gravacao_dados_hd = gravacao_dados_hd
        self.core = core
     
if __name__ == "__main__":
    computador = Placa_mae("Leu memória ram", "Gravou memória ram", "Leu HD", "Gravou Hd", "I7")
    computador2 = Placa_mae("Erro de execusão. Não leu memória ram", "Não gravou memória ram", "Leu HD", "Não gravou Hd", "I3")
    computadores = [computador,computador2]
 
    for componentes in computadores:
        print(f"""{type(componentes).__name__}
        Memória RAM Leitura de Dados: {componentes.leitura_dados_ram}
        Memória RAM Gravação de Dados: {componentes.gravacao_dados_ram}
        HD Leitura de Dados: {componentes.leitura_dados_hd}
        HD Gravação de Dados: {componentes.gravacao_dados_hd}
        Processador: core {componentes.core}""")
 