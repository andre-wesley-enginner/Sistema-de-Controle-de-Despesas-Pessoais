import datetime
from src.classes.categoria import Categoria
from src.classes.despesa import Despesa
from src.classes.receita import Receita
from src.classes.orcamento_mensal import OrcamentoMensal
from src.classes.alerta import Alerta

def setup_function():
    Categoria.lista_categoria.clear()
    Despesa.lista_despesas.clear()
    Receita.lista_receitas.clear()
    OrcamentoMensal.lista_orcamentos.clear()
    Alerta.lista_alertas.clear()

def test_gerar_orcamento_com_alerta():
    cat = Categoria("Alimentação", "despesa", 200, "Comida")
    cat_r = Categoria("Salário", "receita", None, "Salário")

    Receita(1000, datetime.date(2024, 5, 10), cat_r, "Salário", "pix")
    Despesa(300, datetime.date(2024, 5, 12), cat, "Mercado", "debito")

    orc = OrcamentoMensal.gerar_orcamento(5, 2024)

    assert orc.total_despesas == 300
    assert orc.total_receitas == 1000
    assert orc.saldo == 700
    assert len(Alerta.lista_alertas) == 1
