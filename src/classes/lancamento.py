class Lancamento:
    def __init__(self, id, valor, data, categoria, descricao, forma_pagamento):
        self.id = id
        self.valor = valor
        self.data = data
        self.categoria = categoria
        self.descricao = descricao
        self.forma_pagamento = forma_pagamento
        """Constroi um lançamento."""
        pass

    def validar_lancamento(self):
        """Valida os dados do lançamento."""
        pass

    def __str__(self):
        """Retorna uma descrição para o usuário."""
        pass

    def __repr__(self):
        """Retorna uma representação técnica do lançamento."""
        pass

    def __eq__(self, other):
        """Compara dois lançamentos para ver se são iguais ultilizando o id."""
        pass

    def __lt__(self, other):
        """Compara dois lançamentos com base no valor."""
        pass

    def __add__(self, other):
        """Soma o valor dos lançamentos."""
        pass