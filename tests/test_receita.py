import unittest
import json
from datetime import date
from src.classes.receita import Receita, CAMINHO_RECEITA
from src.classes.categoria import Categoria

class TestReceita(unittest.TestCase):

    def setUp(self):
        Receita.lista_receitas.clear()
        Categoria.lista_categoria.clear()

        with open(CAMINHO_RECEITA, "w") as f:
            json.dump([], f)

    def test_criacao_receita(self):
        cat = Categoria("Salário", "receita", None, "Mensal")
        r = Receita(3000, date(2024, 3, 5), cat, "Pagamento", "pix")

        self.assertEqual(r.forma_recebimento, "pix")
        self.assertEqual(r.valor, 3000)

    def test_salvar_e_carregar(self):
        cat = Categoria("Freelancer", "receita", None, "extra")
        Receita(500, date(2024, 3, 10), cat, "Tarefa", "dinheiro")
        Receita.salvar_receitas()

        Receita.lista_receitas.clear()
        Receita.carregar_receitas()

        self.assertEqual(len(Receita.lista_receitas), 1)
