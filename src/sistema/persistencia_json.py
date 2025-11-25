import json
import os

class PersistenciaJSON:
    """Classe responsável por realizar operações de leitura e escrita em arquivos JSON,
    garantindo a persistência dos dados do sistema."""

    def __init__(self, diretorio_dados = "data"):
        self.diretorio_dados = diretorio_dados
        """Inicializa o módulo de persistência definindo o caminho base dos arquivos."""

    def carregar(self, nome_arquivo):
        """Carrega dados de um arquivo JSON. """
        

    def salvar(self, nome_arquivo, dados):
        """ Salva dados em um arquivo JSON. """
        

    def arquivo_existe(self, nome_arquivo):
        """Verifica se um arquivo JSON existe na pasta de dados."""