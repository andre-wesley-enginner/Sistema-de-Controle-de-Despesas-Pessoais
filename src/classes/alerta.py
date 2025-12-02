class Alerta:
    
    def __init__(self, mensagem, tipo, data):
        self.mensagem = mensagem
        self.tipo = tipo
        self.data = data

    def __str__(self):
        return f"[{self.data.isoformat()}] ALERTA ({self.tipo.upper()}): {self.mensagem}"

    def __repr__(self):
        return f"Alerta(mensagem='{self.mensagem}', tipo='{self.tipo}', data='{self.data.isoformat()}')"