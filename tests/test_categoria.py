import pytest
from src.classes.categoria import Categoria

def setup_function():
    Categoria.lista_categoria.clear()

def test_criar_categoria_despesa():
    cat = Categoria("Alimentação", "despesa", 500, "Gastos com comida")
    assert cat.nome == "Alimentação"
    assert cat.tipo == "despesa"
    assert cat.limite == 500

def test_categoria_receita_nao_tem_limite():
    cat = Categoria("Salário", "receita", None, "Salário mensal")
    assert cat.limite is None

def test_categoria_nome_invalido():
    with pytest.raises(ValueError):
        Categoria("", "despesa", 100, "teste")
