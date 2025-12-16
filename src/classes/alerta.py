import json
from datetime import datetime

CAMINHO_ALERTA = "data/alertas.json"

class Alerta:
    lista_alertas = []

    def __init__(self, mensagem, tipo, data=None, id=None):
        if id is None:
            self.id = self.criar_proximo_id()
        else:
            self.id = id
        self.mensagem = mensagem
        self.tipo = tipo
        self.data = data if data is not None else datetime.now()

        Alerta.lista_alertas.append(self)
    def __str__(self):
        return f"[{self.data.strftime('%Y-%m-%d %H:%M:%S')}] ALERTA ({self.tipo.upper()}): {self.mensagem}"

    def __repr__(self):
        return f"Mensagem: {self.mensagem} | Tipo: {self.tipo} | ID: {self.id} | Data: {self.data.strftime('%Y-%m-%d %H:%M:%S')}"
    
    @property
    def mensagem(self):
        return self._mensagem
    
    @mensagem.setter
    def mensagem(self, valor):
        if valor is None:
            raise ValueError("Mensagem não pode ser vazia")
        elif not isinstance(valor, str):
            raise ValueError("Mensagem precisa ser uma string")
        elif valor.strip() == "":
            raise ValueError("Mensagen inválida")
        
        self._mensagem = valor


    @property
    def tipo(self):
        return self._tipo
    
    @tipo.setter
    def tipo(self, valor):
        if valor is None:
            raise ValueError("Tipo não pode ser vazio")
        elif not isinstance(valor, str):
            raise ValueError("Tipo precisa ser uma string")
        elif valor.strip() == "":
            raise ValueError("Tipo inválido")
        
        self._tipo = valor  

    def to_dict(self):
        return{
            "mensagem": self.mensagem,
            "tipo": self.tipo,
            "id": self.id,
            "data": self.data.isoformat()
        }

    @classmethod
    def salvar_alertas(cls):
        with open(CAMINHO_ALERTA, "w", encoding="utf-8") as arq:
            json.dump([alerta.to_dict() for alerta in cls.lista_alertas], arq, indent=4, ensure_ascii=False)
    
    @classmethod
    def carregar_alertas(cls):
        cls.lista_alertas.clear()
        try:
            with open(CAMINHO_ALERTA, "r", encoding="utf-8") as arq:
                dados = json.load(arq)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
        
        for item in dados:
            data_convertida = datetime.fromisoformat(item["data"])
            Alerta(
                mensagem=item["mensagem"],
                tipo=item["tipo"],
                data=data_convertida,
                id=item["id"]
            )

        return cls.lista_alertas

    @classmethod
    def criar_proximo_id(cls):
        try:
            with open(CAMINHO_ALERTA, "r", encoding="utf-8") as arq:
                ids = json.load(arq)
        except (FileNotFoundError, json.JSONDecodeError):
            return 1
        
        if not ids:
            return 1
        
        maior = max(item["id"] for item in ids)
        return maior + 1