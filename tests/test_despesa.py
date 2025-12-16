import pytest
import datetime
from src.classes.categoria import Categoria
from src.classes.despesa import Despesa

def setup_function():
    Categoria.lista_categoria.clear()
    Despesa.lista_despesas.clear()

def test_despesa_forma_pagamento():
    cat = Categoria("Aluguel", "despesa", 1000, "Casa")
    desp = Despesa(800, datetime.date.today(), cat, "Aluguel", "pix")
    assert desp.forma_pagamento == "pix"

def test_forma_pagamento_invalida():
    cat = Categoria("Teste", "despesa", 100, "desc")
    with pytest.raises(ValueError):
        Despesa(50, datetime.date.today(), cat, "teste", "cheque")
