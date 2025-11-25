from categoria import Categoria
from datetime import date, datetime

class Lancamento:
    
    def __init__(self, valor, data, categoria, descricao):
        self.valor = valor
        self.data = data
        self.categoria = categoria
        self.descricao = descricao

    @property
    def valor(self):
        return self._valor
    
    @valor.setter
    def valor(self, dado):
        if not isinstance(dado, (int, float)):
            raise ValueError("Digito Inválido")
        elif dado <= 0:
            raise ValueError("Numero menor ou igual a 0")
        else:
            self._valor = dado

    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, valor):
        if not isinstance(valor, date):
            raise TypeError("A data deve ser fornecida em date.")
        else:
            self._data = valor

    @property
    def categoria(self):
        return self._categoria
    
    @categoria.setter
    def categoria(self, valor):
        if not isinstance(valor, Categoria):
            raise TypeError("Categoria inválida, deve ser um objeto da casse categoria")
        else:
            self._categoria = valor
            
    @property
    def descricao(self):
        return self._descricao
    
    @descricao.setter
    def descricao(self, valor):
        if valor == None or valor.strip() == "":
            raise ValueError("Descrição Inválida")
        else:
            self._descricao = valor 


    def __str__(self):
        return (f"{self.valor} reais, Categoria {self.categoria.nome}, data {self.data}")

    def __repr__(self):
        return (f"valor={self.valor}, data={self.data}, Categoria={self.categoria}, descrição={self.descricao}")


    def __eq__(self, outro):
        if not isinstance(outro, Lancamento):
            return NotImplemented
        return(
        self.valor == outro.valor and
        self.data == outro.data and
        self.categoria == outro.categoria and
        self.descricao == outro.descricao)
                                        
    def criar_lancamento(self):
        pass