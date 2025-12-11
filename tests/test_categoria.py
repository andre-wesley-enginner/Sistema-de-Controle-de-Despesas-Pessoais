import unittest
from src.classes.categoria import Categoria, CAMINHO_CATEGORIA
import os
import json

class TestCategoria(unittest.TestCase):

    def setUp(self):
        # limpa lista antes do teste
        Categoria.lista_categoria.clear()

        # limpa json
        with open(CAMINHO_CATEGORIA, "w") as f:
            json.dump([], f)

    def test_criacao_categoria_despesa(self):
        c = Categoria("Alimentação", "despesa", 500, "Gastos com comida")
        self.assertEqual(c.nome, "Alimentação")
        self.assertEqual(c.tipo, "despesa")
        self.assertEqual(c.limite, 500)

    def test_categoria_receita_sem_limite(self):
        c = Categoria("Salário", "receita", None, "Pagamento mensal")
        self.assertIsNone(c.limite)

    def test_salvar_e_carregar(self):
        Categoria("Aluguel", "despesa", 1000, "Moradia")
        Categoria.salvar_categorias()

        Categoria.lista_categoria.clear()
        Categoria.carregar_categorias()

        self.assertEqual(len(Categoria.lista_categoria), 1)
        self.assertEqual(Categoria.lista_categoria[0].nome, "Aluguel")
