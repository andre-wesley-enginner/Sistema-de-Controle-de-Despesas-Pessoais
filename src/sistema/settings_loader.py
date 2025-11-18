import json

class SettingsLoader:
    """Classe responsável por carregar e gerenciar configurações globais do sistema,
    incluindo parâmetros como limite para alertas, metas mensais e opções de relatórios."""

    def __init__(self, caminho = "data/settings.json"):
        """Inicializa o carregador de configurações com o caminho do arquivo JSON. """
        self.caminho = caminho
        self.settings = {}

    def carregar_settings(self):
        """Carrega o arquivo de configurações settings.json."""
        pass

    def salvar_settings(self):
        """Salva configurações modificadas no arquivo settings.json."""
        pass

    def get_parametro(self, chave, padrao = None):
        """Retorna um parâmetro específico das configurações."""
        pass

    def atualizar_parametro(self, chave, valor):
        """Atualiza um parâmetro do arquivo settings.json."""
        pass
