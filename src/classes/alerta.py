class Alerta:
    """Representa um alerta gerado pelo sistema financeiro."""
    
    def __init__(self, mensagem, tipo, data):
        self.mensagem = mensagem
        self.tipo = tipo
        self.data = data
        """Criar um alerta com msg, tipo e data."""
        

    def exibir_alerta(self):
        """Retorna o alerta como texto para aparecer no menu/print."""