import pytest
from src.classes.categoria import Categoria
from src.classes.relatorio import Relatorio

def test_criar_categoria_sucesso():
    """Verifica se os atributos da categoria são atribuídos corretamente."""
    cat = Categoria(nome="Alimentação", tipo="despesa", limite=500.0, descricao="Mercado")
    assert cat.nome == "Alimentação"
    assert cat.tipo == "despesa"
    assert cat.limite == 500.0

def test_impedir_categoria_duplicada():
    """O sistema deve impedir nomes iguais para o mesmo tipo."""
    Categoria.lista_categoria = [] 
    Categoria("Saúde", "despesa", 100.0, "Descrição Inicial")
    
    with pytest.raises(ValueError):
        Categoria("Saúde", "despesa", 200.0, "Outra Descrição")

def test_receita_sem_limite():
    """Categorias de receita não podem ter limite de gastos."""
    with pytest.raises(ValueError):
        Categoria("Salário", "receita", limite=1000.0, descricao="Meu salário")

def test_limite_categoria_negativo():
    """Garante que não é possível criar categoria com limite negativo."""
    with pytest.raises(ValueError):
        Categoria(nome="Erro", tipo="despesa", limite=-10.0, descricao="Invalido")

def test_calculo_percentual_gasto():
    """Verifica se o cálculo de percentual de gasto por categoria está correto."""
    gasto = 50.0
    limite = 200.0
    
    percentual = Relatorio.calcular_percentual(gasto, limite)
    
    assert percentual == 25.0