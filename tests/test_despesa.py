import pytest
from datetime import date
from src.classes.despesa import Despesa
from src.classes.categoria import Categoria

def test_impedir_despesa_valor_invalido():
    Categoria.lista_categoria = []
    cat = Categoria("Lazer", "despesa", 100.0, "Teste")
    with pytest.raises(ValueError):
        # Adicionada forma_pagamento
        Despesa(valor=0, data=date.today(), categoria=cat, descricao="Teste", forma_pagamento="Dinheiro")

def test_str_despesa():
    Categoria.lista_categoria = []
    cat = Categoria("Saúde", "despesa", 500.0, "Farmácia")
    despesa = Despesa(150.0, date(2025, 12, 16), cat, "Remédios", forma_pagamento="debito")
    assert "150" in str(despesa)