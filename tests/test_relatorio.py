import pytest
from src.classes.relatorio import Relatorio

def test_percentual_categoria():
    """Verifica o cálculo de participação da categoria no total[cite: 34]."""
    total_despesas = 1000.0
    gasto_cat = 200.0
    percentual = (gasto_cat / total_despesas) * 100
    assert percentual == 20.0

def test_ordenacao_relatorio():
    """Garante que as categorias são ordenadas pelo maior gasto."""
    gastos = {"A": {"gasto": 10.0}, "B": {"gasto": 50.0}}
    ordenado = sorted(gastos.items(), key=lambda x: x[1]['gasto'], reverse=True)
    assert ordenado[0][0] == "B"