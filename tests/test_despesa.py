import unittest
import json
from datetime import date
from src.classes.despesa import Despesa, CAMINHO_DESPESA
from src.classes.categoria import Categoria

class TestDespesa(unittest.TestCase):

    def setUp(self):
        Despesa.lista_despesas.clear()
        Categoria.lista_categoria.clear()

        with open(CAMINHO_DESPESA, "w") as f:
            json.dump([], f)

    def test_criacao_despesa(self):
        cat = Categoria("Mercado", "despesa", 800, "Alimentos")
        d = Despesa(120, date(2024, 3, 12), cat, "Compras", "debito")

        self.assertEqual(d.forma_pagamento, "debito")
        self.assertEqual(d.valor, 120)

    def test_salvar_e_carregar(self):
        cat = Categoria("Transporte", "despesa", 300, "Uber")
        Despesa(40, date(2024, 3, 15), cat, "Corrida", "credito")
        Despesa.salvar_despesas()

        Despesa.lista_despesas.clear()
        Despesa.carregar_despesas()

        self.assertEqual(len(Despesa.lista_despesas), 1)
