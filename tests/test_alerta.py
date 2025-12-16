from src.classes.alerta import Alerta
from src.classes.categoria import Categoria

def test_alerta_criacao():
    alerta = Alerta("Mensagem de teste", "limite")
    assert alerta.tipo == "limite"

def test_alerta_limite_excedido_manual():
    Categoria.lista_categoria = []
    cat = Categoria("Lazer", "despesa", 100.0, "Desc")
    # Simulando o que seu código faz no OrcamentoMensal
    mensagem = f"Limite da categoria '{cat.nome}' ultrapassado"
    alerta = Alerta(mensagem=mensagem, tipo="limite")
    assert "Lazer" in alerta.mensagem