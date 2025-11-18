class Despesa:
    def __init__(self, id, valor, data, categoria, descricao, forma_pagamento):
        self.id = id
        self.valor = valor
        self.data = data
        self.categoria = categoria
        self.descricao = descricao
        self.forma_pagamento = forma_pagamento
        """Registra uma nova Despesa com suas características principais"""
        pass

    def validar_despesa(self):
        """Valida os dados da Despesa"""
        pass

    def formatar_despesa(self):
        """Retorna as informações de despesas de forma formatada"""
        pass
        
    def __repr__(self):
        """Retorna a representação técnica da despesa."""
        pass

    def __eq__(self, other):
        """Compara duas despesas para verificar se são iguais utilizando o id das despesas."""
        pass

    def __lt__(self, other):
        """Comparar despesas com base no valor de cada."""
        pass

    def __add__(self, other):
        """Soma o valor das despesas."""
        pass


        
        