import unittest
import json
from datetime import date
from src.classes.lancamento import Lancamento, CAMINHO_LANCAMENTO
from src.classes.categoria import Categoria

class TestLancamento(unittest.TestCase):

    def setUp(self):
        Lancamento.lista_lancamento.clear()
        Categoria.lista_categoria.clear()

        with open(CAMINHO_LANCAMENTO, "w") as f:
            json.dump([], f)

    def test_criacao_lancamento(self):
        cat = Categoria("Alimentação", "despesa", 300, "Comidas")
        l = Lancamento(50, date(2024, 3, 10), cat, "Lanche")

        self.assertEqual(l.valor, 50)
        self.assertEqual(l.categoria.nome, "Alimentação")

    def test_salvar_e_carregar(self):
        cat = Categoria("Alimentação", "despesa", 300, "Comidas")
        Lancamento(60, date(2024, 3, 11), cat, "Almoço")
        Lancamento.salvar_lancamentos()

        Lancamento.lista_lancamento.clear()
        Lancamento.carregar_lancamentos()

        self.assertEqual(len(Lancamento.lista_lancamento), 1)
