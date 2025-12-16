import pytest
from src.classes.alerta import Alerta

def setup_function():
    Alerta.lista_alertas.clear()

def test_criar_alerta():
    alerta = Alerta("Limite estourado", "limite")
    assert alerta.mensagem == "Limite estourado"
    assert alerta.tipo == "limite"

def test_alerta_mensagem_vazia():
    with pytest.raises(ValueError):
        Alerta("", "limite")
