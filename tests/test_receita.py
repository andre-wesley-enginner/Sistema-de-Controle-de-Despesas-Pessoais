import pytest
from datetime import date
from src.classes.receita import Receita
from src.classes.categoria import Categoria

def test_criar_receita_sucesso():
    Categoria.lista_categoria = []
    cat = Categoria("Salário", "receita", 0.0, "Mensal")
    rec = Receita(5000.0, date.today(), cat, "Pagamento", forma_recebimento="PIX")
    assert rec.valor == 5000.0

def test_comparar_receitas_iguais():
    Categoria.lista_categoria = []
    cat = Categoria("Bônus", "receita", 0.0, "Extra")
    rec1 = Receita(100.0, date(2025, 12, 1), cat, "Extra", forma_recebimento="Dinheiro")
    assert rec1 == rec1