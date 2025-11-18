class OrcamentoMensal:
    def __init__(self, ano, mes, lancamento, limite_total):
        self.ano = ano
        self.mes = mes
        self.lancamento = lancamento 
        self.limite_total = limite_total
        """Gerencia o orçamento financeiro de um mês específico, incluindo receitas,
        despesas, saldo disponível e limites estabelecidos."""
        pass
    
    def calcular_total_receitas(self):
        """Inicializa um orçamento mensal com ano, mês, lançamentos e limite total."""
        pass

    def calcular_total_despesas(self):
        """Calcula o valor total de todas as receitas do mês."""
        pass
    
    def saldo_disponivel(self):
        """Calcula o quanto ainda está disponível no orçamento mensal."""
        pass

    def registrar_lancamento(self, lancamento):
        """Adiciona um novo lançamento (receita ou despesa) ao orçamento do mês."""
        pass

    def categorias_acima_limite(self):
        """Verifica quais categorias ultrapassaram seus limites mensais."""
        pass