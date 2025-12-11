from lancamento import Lancamento
from despesa import Despesa
from receita import Receita
from datetime import date, datetime

class OrcamentoMensal:
    
    def __init__(self, ano, mes, lista_lancamentos=None, limite_total=0):
        self.ano = ano
        self.mes = mes
        self.lista_lancamentos = lista_lancamentos or []
        self.limite_total = limite_total
    
    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, valor):
        if not isinstance(valor, int):
            raise ValueError("O ano deve ser um número inteiro")
        if valor < 2000 or valor > 3000:
            raise ValueError("Ano inválido, fora de um intervalo razoável")
        self._ano = valor

    @property
    def mes(self):
        return self._mes
    
    @mes.setter
    def mes(self, valor):
        if not isinstance(valor, int) or not (1 <= valor <= 12):
            raise ValueError("Mês invalido, deve ser um número inteiro de 1 a 12")
        self._mes = valor

    def adicionar_lancamento(self, lancamento):
        if not isinstance(lancamento, Lancamento):
            raise TypeError("O item adicionado deve ser um lançamento.")
        
        if lancamento.data.year != self.ano or lancamento.data.month != self.mes:
            raise ValueError(f"Lançamento fora do período deste Orçamento: {self.mes}/{self.ano}")
        
        self.lista_lancamentos.append(lancamento)

    def calcular_total_receitas(self):
        total = 0.0
        for lancamento in self.lista_lancamentos:
            if isinstance(lancamento, Receita):
                total += lancamento.valor
        return total

    def calcular_total_despesas(self):
        total = 0.0
        for lancamento in self.lista_lancamentos:
            if isinstance(lancamento, Despesa):
                total += lancamento.valor
        return total
        
    
    def saldo_disponivel(self):
        total_receitas = self.calcular_total_receitas()
        total_despesas = self.calcular_total_despesas()
        saldo = total_receitas - total_despesas

        if saldo < 0:
            print(f"Alerta: Déficit Orçamento! Saldo negativo de R${abs(saldo):.2f}.") 
        
        return saldo 
    
    def total_despesas_por_categoria(self):
        totais_por_categoria = {}
        for lancamento in self.lista_lancamentos:
            if isinstance(lancamento, Despesa):
                nome_categoria = lancamento.categoria.nome
                totais_por_categoria[nome_categoria] = totais_por_categoria.get(nome_categoria, 0.0) + lancamento.valor
        return totais_por_categoria
            