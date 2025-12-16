import pytest
import datetime
from src.classes.categoria import Categoria
from src.classes.lancamento import Lancamento

def setup_function():
    Categoria.lista_categoria.clear()
    Lancamento.lista_lancamento.clear()

def test_criar_lancamento():
    cat = Categoria("Transporte", "despesa", 200, "Ônibus")
    lanc = Lancamento(50, datetime.date(2024, 5, 10), cat, "Passagem")
    assert lanc.valor == 50
    assert lanc.categoria == cat

def test_valor_invalido():
    cat = Categoria("Teste", "despesa", 100, "desc")
    with pytest.raises(ValueError):
        Lancamento(-10, datetime.date.today(), cat, "erro")
