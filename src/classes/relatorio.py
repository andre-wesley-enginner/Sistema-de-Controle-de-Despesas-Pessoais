class Relatorio:
    def __init__(self, orcamento_atual, historico_meses):
        self.orcamento_atual = orcamento_atual
        self.historico_meses = historico_meses
        """Inicializa o relatório com o orçamento atual e o histórico."""
        pass

    def calcular_total_por_categoria(self):
        """Calcula o valor total gasto por categoria no mês atual."""
        pass

    def totais_por_pagamento(self):
        """Agrupa os lançamentos do mês atual por forma de pagamento."""
        pass

    def percentual_por_categoria(self):
        """Calcula qual porcentagem do total de despesas cada categoria representa."""
        pass

    def comparar_ultimos_meses(self):
        """Compara o total de despesas dos últimos meses registrados."""
        pass

    def encontrar_mes_mais_economico(self):
        """Encontra o mês com menor total de despesas no histórico."""
        pass