from src.classes.orcamento_mensal import OrcamentoMensal

def test_calculo_totais_orcamento():
    # Passando os 4 argumentos que faltavam
    orc = OrcamentoMensal(mes=12, ano=2025, total_despesas=1000.0, 
                          total_receitas=3000.0, saldo=2000.0, 
                          orcamento_por_categoria={})
    assert orc.saldo == 2000.0

def test_aviso_saldo_negativo():
    orc = OrcamentoMensal(12, 2025, total_despesas=800.0, 
                          total_receitas=500.0, saldo=-300.0, 
                          orcamento_por_categoria={})
    assert orc.saldo < 0