from lancamento import Lancamento

class Despesa(Lancamento):
    
    def __init__(self, valor, data, categoria, descricao, forma_pagamento):
        super().__init__(valor, data, categoria, descricao)
        self.forma_pagamento = forma_pagamento

    @property
    def forma_pagamento(self):
        return self._forma_pagamento
    
    @forma_pagamento.setter
    def forma_pagamento(self, valor):
        metodos = ["dinheiro", "debito", "credito", "pix"]
        if valor == None:
            raise ValueError("Método Inválido")
        elif not isinstance(valor, str):
            raise TypeError("Método deve ser passado em String")
        if valor.strip() == "":
            raise ValueError("Método Inválido")
        valor = valor.lower()
        if valor not in metodos:
            raise ValueError("Método Inválido")
        else:
            self._forma_pagamento = valor 

    def __str__(self):
        return (f"Despesa de {self.valor}, Categoria {self.categoria.nome}, data {self.data}, forma de pagamento {self.forma_pagamento}, descrição {self.descricao}")
    
    def __eq__(self, outro):
        if not isinstance(outro, Despesa):
            return NotImplemented
        return(
        self.valor == outro.valor and
        self.data == outro.data and
        self.categoria == outro.categoria and
        self.descricao == outro.descricao and
        self.forma_pagamento == outro.forma_pagamento)
    
    def __repr__(self):
        return (f"valor={self.valor}, data={self.data}, Categoria={self.categoria}, forma de pagamento {self.forma_pagamento},  descrição={self.descricao}")
        

    def verificar_categoria(self):
        pass

    def verificar_limite(self):
        pass   