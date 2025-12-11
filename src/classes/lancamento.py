from .categoria import Categoria
from datetime import date, datetime
import json

CAMINHO_LANCAMENTO = "data/lancamentos.json"

class Lancamento:

    lista_lancamento = []
    def __init__(self, valor, data, categoria, descricao, id=None):
        if id is None:
            self.id = self.criar_proximo_id()
        else:
            self.id = id
        self.valor = valor
        self.data = data
        self.categoria = categoria
        self.descricao = descricao
        Lancamento.lista_lancamento.append(self)

    @property
    def valor(self):
        return self._valor
    
    @valor.setter
    def valor(self, dado):
        if not isinstance(dado, (int, float)):
            raise ValueError("Digito Inválido")
        elif dado <= 0:
            raise ValueError("Numero menor ou igual a 0")
        else:
            self._valor = dado

    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, valor):
        if not isinstance(valor, date):
            raise TypeError("A data deve ser fornecida em date.")
        else:
            self._data = valor

    @property
    def categoria(self):
        return self._categoria
    
    @categoria.setter
    def categoria(self, valor):
        if not isinstance(valor, Categoria):
            raise TypeError("Categoria inválida, deve ser um objeto da classe categoria")
        else:
            self._categoria = valor
            
    @property
    def descricao(self):
        return self._descricao
    
    @descricao.setter
    def descricao(self, valor):
        if valor == None or valor.strip() == "":
            raise ValueError("Descrição Inválida")
        else:
            self._descricao = valor 


    def __str__(self):
        return (f"{self.valor} reais, Categoria {self.categoria.nome}, data {self.data}")

    def __repr__(self):
        return (f"valor={self.valor}, data={self.data}, Categoria={self.categoria}, descrição={self.descricao}")


    def __eq__(self, outro):
        if not isinstance(outro, Lancamento):
            return NotImplemented
        return self.id == outro.id

    
    def to_dict(self):
        return {
            "id": self.id,
            "valor": self.valor,
            "data": self.data.isoformat(),
            "descricao": self.descricao,
            "categoria": self.categoria.to_dict()
        }
                                 
    @classmethod
    def criar_proximo_id(cls):
        try:
            with open(CAMINHO_LANCAMENTO, "r", encoding="utf-8") as arq:
                ids = json.load(arq)
                
        except (FileNotFoundError, json.JSONDecodeError):
            return 1
        
        if not ids:
            return 1
        
        maior_id = max(item["id"] for item in ids)
        return maior_id + 1   

    @classmethod
    def salvar_lancamentos(cls):
        with open(CAMINHO_LANCAMENTO, "w", encoding="utf-8") as arq:
            json.dump([lancamento.to_dict() for lancamento in cls.lista_lancamento]
                      , arq, indent=4, ensure_ascii=False)
            
    @classmethod
    def carregar_lancamentos(cls):
        Categoria.carregar_categorias()
        cls.lista_lancamento.clear()
        try:
            with open(CAMINHO_LANCAMENTO, "r", encoding="utf-8") as arq:
                dados = json.load(arq)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
        for item in dados:
            cat = next((c for c in Categoria.lista_categoria if c.id == item["categoria"]["id"]),None)
            if cat is None:
                cat = Categoria(
                    nome=item["categoria"]["nome"],
                    tipo=item["categoria"]["tipo"],
                    limite=item["categoria"]["limite"],
                    descricao=item["categoria"]["descricao"],
                    id=item["categoria"]["id"]
                )

            Lancamento(
                valor=item["valor"],
                data=datetime.fromisoformat(item["data"]).date(),
                categoria=cat,
                descricao=item["descricao"],
                id=item["id"]
            )
        return cls.lista_lancamento

    @classmethod
    def editar_lancamentos(cls):
        Categoria.carregar_categorias()
        cls.carregar_lancamentos()

        if not cls.lista_lancamento:
            print("Nenhum lançamento cadastrado.")
            return

        print("\nLançamentos disponíveis:")
        for lanc in cls.lista_lancamento:
            print(f"ID: {lanc.id} | Valor: {lanc.valor} | Data: {lanc.data} | Categoria: {lanc.categoria.nome}")

        try:
            id_escolhido = int(input("\nDigite o ID do lançamento que deseja editar: "))
        except ValueError:
            print("ID inválido.")
            return

        lancamento = next((c for c in cls.lista_lancamento if c.id == id_escolhido), None)

        if lancamento is None:
            print("Lançamento não encontrado.")
            return

        while True:
            print("\nO que deseja editar?")
            print("1 - Valor")
            print("2 - Data")
            print("3 - Categoria")
            print("4 - Descrição")
            print("0 - Concluir edição")

            opcao = input("Escolha: ")

            try:
                if opcao == "1":
                    novo = float(input("Novo valor: "))
                    lancamento.valor = novo

                elif opcao == "2":
                    novo = input("Nova data (YYYY-MM-DD): ")
                    lancamento.data = datetime.strptime(novo, "%Y-%m-%d").date()

                elif opcao == "3":
                    print("\nCategorias disponíveis:")
                    for c in Categoria.lista_categoria:
                        print(f"ID: {c.id} | Nome: {c.nome} | Tipo: {c.tipo}")

                    try:
                        id_cat = int(input("Digite o ID da nova categoria: "))
                    except ValueError:
                        print("ID inválido.")
                        continue

                    nova_cat = next((c for c in Categoria.lista_categoria if c.id == id_cat), None)

                    if nova_cat is None:
                        print("Categoria não encontrada.")
                        continue

                    lancamento.categoria = nova_cat

                elif opcao == "4":
                    novo = input("Nova descrição: ")
                    lancamento.descricao = novo

                elif opcao == "0":
                    break

                else:
                    print("Opção inválida.")
                    continue

            except Exception as e:
                print("Erro ao editar:", e)
                continue

        cls.salvar_lancamentos()
        print("\nLançamento atualizado com sucesso!")