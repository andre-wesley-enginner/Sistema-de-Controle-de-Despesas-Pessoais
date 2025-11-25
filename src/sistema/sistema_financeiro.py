class SistemaFinanceiro:
    """Classe responsável por organizar todas as operações do sistema de controle de despesas pessoais.
    Ela centraliza o uso das outras classes, incluindo categorias, lançamentos, relatórios,
    orçamento mensal, alertas e persistência."""

    def __init__(self, persistencia, settings_loader):
        """Inicializa o sistema financeiro, recebendo módulos de persistência e de configurações."""
        self.persistencia = persistencia
        self.settings_loader = settings_loader
        self.categorias = []
        self.lancamentos = []
        self.orcamentos = {}
        self.alertas = []

    def carregar_dados(self):
        """Carrega categorias, lançamentos, orçamentos e configurações dos arquivos JSON."""
        

    def salvar_dados(self):
        """ Salva todos os dados manipulados pelo sistema nos arquivos JSON."""
        

    def adicionar_categoria(self, categoria):
        """Adiciona uma nova categoria ao sistema."""
        

    def remover_categoria(self, nome):
        """Remove uma categoria pelo nome, caso ela não tenha lançamentos associados."""
        

    def adicionar_lancamento(self, lancamento):
        """Adiciona um lançamento (receita ou despesa) ao sistema."""
        

    def listar_lancamentos(self, mes = None, ano = None):
        """Lista lançamentos filtrados por mês e ano."""
        

    def calcular_saldo_mensal(self, mes, ano):
        """Calcula o saldo mensal (receitas - despesas)."""
        

    def gerar_relatorio_categorias(self, mes, ano):
        """Gera relatório com total de despesas agrupadas por categoria."""
        

    def gerar_relatorio_pagamentos(self, mes, ano):
        """Gera relatório agrupando despesas pela forma de pagamento."""
        

    def gerar_comparativo_mensal(self, quantidade_meses):
        """Gera um comparativo entre receitas e despesas dos últimos meses."""
        

    def verificar_alertas(self, lancamento):
        """Verifica se um lançamento gera alertas:"""