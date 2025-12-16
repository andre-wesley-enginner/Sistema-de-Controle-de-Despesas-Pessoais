import pytest
from datetime import date
from src.classes.despesa import Despesa
from src.classes.categoria import Categoria
from src.classes.lancamento import Lancamento

def test_validacao_tipo_data():
    """Garante que a data deve ser fornecida em formato date[cite: 53]."""
    cat = Categoria("Outros", "DESPESA", 10.0)
    with pytest.raises(TypeError):
        Despesa(10.0, "2025-12-16", cat, "Erro de tipo")

def test_heranca_lancamento():
    """Verifica se uma Despesa herda corretamente os atributos de Lancamento[cite: 46, 47]."""
    cat = Categoria("Educação", "DESPESA", 1000.0)
    data_hoje = date.today()
    desp = Despesa(300.0, data_hoje, cat, "Mensalidade")
    
    assert isinstance(desp, Lancamento)
    assert desp.valor == 300.0
    assert desp.data == data_hoje