import pytest
import datetime
from src.classes.categoria import Categoria
from src.classes.receita import Receita

def setup_function():
    Categoria.lista_categoria.clear()
    Receita.lista_receitas.clear()

def test_criar_receita():
    cat = Categoria("Salário", "receita", None, "Salário mensal")
    rec = Receita(3000, datetime.date.today(), cat, "Pagamento", "pix")
    assert rec.valor == 3000
    assert rec.forma_recebimento == "pix"
