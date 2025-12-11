import json
import datetime

from .receita import Receita
from .despesa import Despesa
from .categoria import Categoria

CAMINHO_RELATORIO = "data/relatorios.json"

class Relatorio:

    lista_relatorios = []

    def __init__(self, mes, ano, total_receitas, total_despesas, saldo, total_por_categoria, id=None):
        self.mes = mes
        self.ano = ano
        self.total_receitas = total_receitas
        self.total_despesas = total_despesas
        self.saldo = saldo
        self.total_por_categoria = total_por_categoria
        self.id = id if id is not None else self.criar_proximo_id()

        Relatorio.lista_relatorios.append(self)

    # ============================================================
    # ===============  MÉTODOS PRINCIPAIS DO RELATÓRIO  ==========
    # ============================================================

    @classmethod
    def gerar_relatorio_mensal(cls, mes, ano):
        """
        Gera o relatório básico da Semana 3
        """

        Categoria.carregar_categorias()
        Receita.carregar_receitas()
        Despesa.carregar_despesas()

        # Filtrar receitas e despesas do mês
        receitas_mes = [r for r in Receita.lista_receitas if r.data.month == mes and r.data.year == ano]
        despesas_mes = [d for d in Despesa.lista_despesas if d.data.month == mes and d.data.year == ano]

        total_receitas = sum(r.valor for r in receitas_mes)
        total_despesas = sum(d.valor for d in despesas_mes)
        saldo = total_receitas - total_despesas

        # Total por categoria (despesas)
        total_por_categoria = {}
        for desp in despesas_mes:
            nome = desp.categoria.nome
            total_por_categoria[nome] = total_por_categoria.get(nome, 0) + desp.valor

        # Criar relatório
        rel = Relatorio(
            mes=mes,
            ano=ano,
            total_receitas=total_receitas,
            total_despesas=total_despesas,
            saldo=saldo,
            total_por_categoria=total_por_categoria,
        )

        cls.salvar_relatorios()
        return rel

    # ============================================================
    # ========================= JSON =============================
    # ============================================================

    def to_dict(self):
        return {
            "id": self.id,
            "mes": self.mes,
            "ano": self.ano,
            "total_receitas": self.total_receitas,
            "total_despesas": self.total_despesas,
            "saldo": self.saldo,
            "total_por_categoria": self.total_por_categoria
        }

    @classmethod
    def salvar_relatorios(cls):
        with open(CAMINHO_RELATORIO, "w", encoding="utf-8") as arq:
            json.dump([r.to_dict() for r in cls.lista_relatorios],
                      arq, indent=4, ensure_ascii=False)

    @classmethod
    def carregar_relatorios(cls):
        cls.lista_relatorios.clear()
        try:
            with open(CAMINHO_RELATORIO, "r", encoding="utf-8") as arq:
                dados = json.load(arq)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

        for item in dados:
            Relatorio(
                mes=item["mes"],
                ano=item["ano"],
                total_receitas=item["total_receitas"],
                total_despesas=item["total_despesas"],
                saldo=item["saldo"],
                total_por_categoria=item["total_por_categoria"],
                id=item["id"],
            )
        return cls.lista_relatorios

    # ============================================================
    # ========================= ID ===============================
    # ============================================================

    @classmethod
    def criar_proximo_id(cls):
        try:
            with open(CAMINHO_RELATORIO, "r", encoding="utf-8") as arq:
                dados = json.load(arq)
        except (FileNotFoundError, json.JSONDecodeError):
            return 1

        if not dados:
            return 1

        maior = max(item["id"] for item in dados)
        return maior + 1

    # ============================================================
    # =================== IMPRESSÃO FORMATADA =====================
    # ============================================================

    def exibir(self):
        print("\n===== RELATÓRIO MENSAL =====")
        print(f"Mês/Ano: {self.mes}/{self.ano}")
        print(f"Total Receitas: R$ {self.total_receitas:.2f}")
        print(f"Total Despesas: R$ {self.total_despesas:.2f}")
        print(f"Saldo: R$ {self.saldo:.2f}")
        print("\n--- Total por Categoria ---")
        for cat, total in self.total_por_categoria.items():
            print(f"{cat}: R$ {total:.2f}")
        print("============================\n")
