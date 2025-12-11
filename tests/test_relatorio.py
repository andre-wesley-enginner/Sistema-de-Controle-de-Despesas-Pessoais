import unittest
import json
from datetime import date
from src.classes.relatorio import Relatorio, CAMINHO_RELATORIO
from src.classes.categoria import Categoria
from src.classes.receita import Receita, CAMINHO_RECEITA
from src.classes.despesa import Despesa, CAMINHO_DESPESA

class TestRelatorio(unittest.TestCase):

    def setUp(self):
        # limpar listas
        Relatorio.lista_relatorios.clear()
        Categoria.lista_categoria.clear()
        Receita.lista_receitas.clear()
        Despesa.lista_despesas.clear()

        # limpar jsons
        for caminho in [CAMINHO_RECEITA, CAMINHO_DESPESA, "data/categorias.json", CAMINHO_RELATORIO]:
            with open(caminho, "w") as f:
                json.dump([], f)

        # categorias
        self.cat_sal = Categoria("Salário", "receita", None, "Mensal")
        self.cat_mer = Categoria("Mercado", "despesa", 600, "Compras")

        # receitas
        Receita(3000, date(2024, 3, 5), self.cat_sal, "Pagamento", "pix")
        Receita(500, date(2024, 3, 10), self.cat_sal, "Extra", "dinheiro")
        Receita.salvar_receitas()

        # despesas
        Despesa(200, date(2024, 3, 12), self.cat_mer, "Supermercado", "debito")
        Despesa(100, date(2024, 3, 15), self.cat_mer, "Feira", "pix")
        Despesa.salvar_despesas()
        
    def test_relatorio_mensal(self):
        rel = Relatorio.gerar_relatorio_mensal(3, 2024)

        self.assertEqual(rel.total_receitas, 3500)
        self.assertEqual(rel.total_despesas, 300)
        self.assertEqual(rel.saldo, 3200)
        self.assertEqual(rel.total_por_categoria["Mercado"], 300)

    def test_salvar_e_carregar_relatorios(self):
        rel = Relatorio.gerar_relatorio_mensal(3, 2024)
        Relatorio.salvar_relatorios()

        Relatorio.lista_relatorios.clear()
        Relatorio.carregar_relatorios()

        self.assertEqual(len(Relatorio.lista_relatorios), 1)
