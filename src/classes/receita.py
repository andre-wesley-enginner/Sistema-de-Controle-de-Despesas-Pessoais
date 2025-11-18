class Receita:
    """Representa uma receita financeira."""
    
    def __init__(self, id, valor, data, categoria, descricao, forma_pagamento):
        self.id = id
        self.valor = valor
        self.data = data
        self.categoria = categoria
        self.descricao = descricao
        self.forma_pagamento = forma_pagamento
        """Registra uma nova Receita com suas características principais."""
        pass

    def validar_receita(self):
        """Valida os dados da Receita."""
        pass

    def formatar_receita(self):
        """Retorna as informações da receita de forma formatada."""
        pass
        
    def __repr__(self):
        """Retorna a representação técnica da receita."""
        pass

    def __eq__(self, other):
        """Compara duas receitas para verificar se são iguais ultilizando o id."""
        pass

    def __it__(self, other):
        """Compara duas receitas pelo valor."""
        pass

    def __add__(self, other):
        """Soma o valor das receitas"""
        pass