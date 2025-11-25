class Categoria:
    
    def __init__(self, nome, tipo, limite, descricao):
        self.nome = nome
        self.tipo = tipo
        self.limite = limite
        self.descricao = descricao

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        if valor == None or valor.strip() == "":
            raise ValueError("Nome Inválido.")
        else:
            self._nome = valor
        
    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, valor):
        tipos = ["despesa", "receita"]
        if valor == None or valor.strip() == "":
            raise ValueError("Tipo inválido")
        valor = valor.lower()
        if valor not in tipos:
            raise ValueError("Tipo inválido")
        else:
            self._tipo = valor

    @property
    def limite(self):
        return self._limite
    
    @limite.setter
    def limite(self, valor):
        if valor < 0:
            raise ValueError("O valor não pode ser negativo")
        else:
            self._limite = valor

    @property
    def descricao(self):
        return self._descricao
    
    @descricao.setter
    def descricao(self, valor):
        if valor == None or valor.strip() == "":
            raise ValueError("Categoria sem descrição")
        else:
            self._descricao = valor

    def __str__(self):
        return (f"{self.nome}, {self.tipo}, {self.limite}, {self.descricao}")

    def __eq__(self, outro):
        if not isinstance(outro, Categoria):
           return NotImplemented
        return self.nome == outro.nome
            
    def salvar_categoria(self):
        pass

    def editar_categoria(self):
        pass

    def excluir_categoria(self):
        pass