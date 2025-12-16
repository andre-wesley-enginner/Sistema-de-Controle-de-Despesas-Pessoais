import json
from .alerta import Alerta
from .despesa import Despesa
from .receita import Receita
from .lancamento import Lancamento
from .relatorio import Relatorio
from .categoria import Categoria

CAMINHO_ORCAMENTO = "data/orcamentos.json"

class OrcamentoMensal:
    lista_orcamentos = []

    def __init__(self, mes, ano, total_despesas, total_receitas, saldo, orcamento_por_categoria, id=None):
        self.id = id if id is not None else self.criar_proximo_id()
        self.mes = mes
        self.ano = ano
        self.total_despesas = total_despesas
        self.total_receitas = total_receitas
        self.saldo = saldo
        self.orcamento_por_categoria = orcamento_por_categoria

        OrcamentoMensal.lista_orcamentos.append(self)

    @property
    def mes(self):
        return self._mes
    
    @mes.setter
    def mes(self, valor):
        if not isinstance(valor, int):
            raise ValueError("Mês deve ser um número inteiro")
        if valor < 1 or valor > 12:
            raise TypeError("Mês inválido")
        else:
            self._mes = valor

    @property 
    def ano(self):
        return self._ano
    
    @ano.setter
    def ano(self, valor):
        if not isinstance(valor, int):
            raise ValueError("Ano deve ser inteiro")
        if valor < 2000 or valor > 3000:
            raise TypeError("Ano inválido")
        else:
            self._ano = valor

    def __str__(self):
        return (
            f"Orcamento {self.mes}/{self.ano} |"
            f"Receitas: {self.total_receitas} |"
            f"Despesas: {self.total_despesas} |"
            f"Saldo: {self.saldo}"
        )
    
    def to_dict(self):
        return{
            "id": self.id,
            "mes": self.mes,
            "ano": self.ano,
            "total_despesas": self.total_despesas,
            "total_receitas": self.total_receitas,
            "saldo": self.saldo,
            "orcamento_por_categoria": self.orcamento_por_categoria
        }
    
    @classmethod
    def salvar_orcamentos(cls):
        with open(CAMINHO_ORCAMENTO, "w", encoding="utf-8") as arq:
            json.dump([orc.to_dict() for orc in cls.lista_orcamentos], arq, indent=4, ensure_ascii=False)

    @classmethod
    def carregar_orcamentos(cls):
        try:
            with open(CAMINHO_ORCAMENTO, "r", encoding="utf-8") as arq:
                dados = json.load(arq)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
        
        for item in dados:
            OrcamentoMensal(
            mes=item["mes"],
            ano=item["ano"],
            total_despesas=item["total_despesas"],
            total_receitas=item["total_receitas"],
            saldo=item["saldo"],
            orcamento_por_categoria=item["orcamento_por_categoria"],
            id=item["id"]
            )

        return cls.lista_orcamentos
    
    @classmethod
    def criar_proximo_id(cls):
        try:
            with open(CAMINHO_ORCAMENTO, "r", encoding="utf-8") as arq:
                ids = json.load(arq)
        except (FileNotFoundError, json.JSONDecodeError):
            return 1
        
        if not ids:
            return 1

        return max(item["id"] for item in ids) + 1

    @classmethod
    def _gerar_alertas(cls, orcamento_por_categoria, saldo, mes, ano):
        for categoria, dados in orcamento_por_categoria.items():
            if dados["limite"] is not None and dados["gasto"] > dados["limite"]:
                Alerta(
                    mensagem=f"Limite da categoria '{categoria}' ultrapassado em {mes}/{ano}",
                    tipo="limite"
                )
        if saldo < 0:
            Alerta(
                mensagem=f"Saldo negativo no orçamento de {mes}/{ano}",
                tipo="saldo"
            )
        
        Alerta.salvar_alertas()

    @classmethod
    def gerar_orcamento(cls, mes, ano):

        cls.lista_orcamentos = [o for o in cls.lista_orcamentos if not (o.mes == mes and o.ano == ano)]

        despesas_mes = [
            d for d in Despesa.lista_despesas
            if d.data.month == mes and d.data.year == ano
        ]
        receitas_mes = [
            r for r in Receita.lista_receitas
            if r.data.month == mes and r.data.year == ano
        ]

        total_despesas = sum(d.valor for d in despesas_mes)
        total_receitas = sum(r.valor for r in receitas_mes)
        saldo = total_receitas - total_despesas

        orcamento_por_categoria = {}
        for categoria in Categoria.lista_categoria:
            if categoria.tipo == "despesa":
                despesas_categoria = [
                    d for d in despesas_mes if d.categoria.id == categoria.id
                ]
                total_categoria = sum(d.valor for d in despesas_categoria)

                percentual = (
                    (total_categoria / categoria.limite) * 100
                    if categoria.limite and categoria.limite > 0 else 0
                )

                orcamento_por_categoria[categoria.nome] = {
                    "limite": categoria.limite,
                    "gasto": total_categoria,
                    "percentual": round(percentual, 2)
                }

        cls._gerar_alertas(orcamento_por_categoria, saldo, mes, ano)

        orcamento = OrcamentoMensal(
            mes=mes,
            ano=ano,
            total_despesas=total_despesas,
            total_receitas=total_receitas,
            saldo=saldo,
            orcamento_por_categoria=orcamento_por_categoria
        )
        
        cls.salvar_orcamentos()
        return orcamento