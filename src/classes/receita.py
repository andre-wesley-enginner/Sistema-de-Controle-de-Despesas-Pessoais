from lancamento import Lancamento

class Receita(Lancamento):
    
    
    def __init__(self, valor, data, categoria, descricao, forma_recebimento):
        super().__init__(valor, data, categoria, descricao)
        self.forma_recebimento = forma_recebimento

    @property
    def forma_recebimento(self):
        return self._forma_recebimento
    
    @forma_recebimento.setter
    def forma_recebimento(self, valor):
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
            self._forma_recebimento = valor  
        
    def __str__(self):
        return (f"Receita de {self.valor}, Categoria {self.categoria.nome}, data {self.data}, forma de recebimento {self.forma_recebimento}, descrição {self.descricao}")
    
    def __eq__(self, outro):
        if not isinstance(outro, Receita):
            return NotImplemented
        return(
        self.valor == outro.valor and
        self.data == outro.data and
        self.categoria == outro.categoria and
        self.descricao == outro.descricao and
        self.forma_recebimento == outro.forma_recebimento)
    
    def __repr__(self):
        return (f"valor={self.valor}, data={self.data}, Categoria={self.categoria}, forma de recebimento {self.forma_recebimento},  descrição={self.descricao}")


    def verificar_categoria(self):
        pass
    
    def verificar_meta(self):
        pass