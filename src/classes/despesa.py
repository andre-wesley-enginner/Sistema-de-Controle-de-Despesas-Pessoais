from .lancamento import Lancamento
import json
from .categoria import Categoria
import datetime
CAMINHO_DESPESA = "data/despesas.json"

class Despesa(Lancamento):
    lista_despesas = []
    def __init__(self, valor, data, categoria, descricao, forma_pagamento, id=None):
        super().__init__(valor, data, categoria, descricao, id=id)
        self.forma_pagamento = forma_pagamento
        Despesa.lista_despesas.append(self)

    @property
    def forma_pagamento(self):
        return self._forma_pagamento
    
    @forma_pagamento.setter
    def forma_pagamento(self, valor):
        metodos = ["dinheiro", "debito", "credito", "pix"]
        if valor == None:
            raise ValueError("Método Inválido")
        elif not isinstance(valor, str):
            raise TypeError("Método deve ser passado em String")
        if valor.strip() == "":
            raise ValueError("Método Inválido")
        valor = valor.lower()
        if valor not in metodos:
            raise ValueError("Método Inválido")
        else:
            self._forma_pagamento = valor 

    def __str__(self):
        return (f"Despesa de {self.valor}, Categoria {self.categoria.nome}, data {self.data}, forma de pagamento {self.forma_pagamento}, descrição {self.descricao}")
    
    def __eq__(self, outro):
        if not isinstance(outro, Despesa):
            return NotImplemented
        return self.id == outro.id
    
    def __repr__(self):
        return (f"valor={self.valor}, data={self.data}, Categoria={self.categoria}, forma de pagamento {self.forma_pagamento},  descrição={self.descricao}")
        
    def to_dict(self):
        d = super().to_dict()
        d["forma_pagamento"] = self.forma_pagamento
        return d
    
    @classmethod
    def salvar_despesas(cls):
        with open(CAMINHO_DESPESA, "w", encoding="utf-8") as arq:
            json.dump([despesa.to_dict() for despesa in cls.lista_despesas]
                      , arq, indent=4, ensure_ascii=False)

    @classmethod
    def carregar_despesas(cls):
        Categoria.carregar_categorias()
        cls.lista_despesas.clear()

        try:
            with open(CAMINHO_DESPESA, "r", encoding="utf-8") as arq:
                dados = json.load(arq)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

        for item in dados:
            cat = next((c for c in Categoria.lista_categoria if c.id == item["categoria"]["id"]), None)

            if cat is None:
                cat = Categoria(
                    nome=item["categoria"]["nome"],
                    tipo=item["categoria"]["tipo"],
                    limite=item["categoria"]["limite"],
                    descricao=item["categoria"]["descricao"],
                    id=item["categoria"]["id"]
                )

            Despesa(
                valor=item["valor"],
                data=datetime.date.fromisoformat(item["data"]),
                categoria=cat,
                descricao=item["descricao"],
                forma_pagamento=item["forma_pagamento"],
                id=item["id"]
            )

        return cls.lista_despesas

    @classmethod
    def criar_despesa(cls):
        cls.carregar_despesas()
        Categoria.carregar_categorias()

        try:
            valor = float(input("Valor da despesa: "))
            if valor <= 0: raise ValueError("O valor deve ser positivo.")
            
            data_str = input("Data (AAAA-MM-DD): ")
            dt = datetime.date.fromisoformat(data_str)
            
            categorias_despesa = [c for c in Categoria.lista_categoria if c.tipo == "despesa"]
            if not categorias_despesa:
                print("Erro: Crie uma categoria de despesa primeiro.")
                return

            for c in categorias_despesa: print(f"ID: {c.id} | Nome: {c.nome}")
            id_cat = int(input("ID da categoria: "))
            cat_escolhida = next((c for c in categorias_despesa if c.id == id_cat), None)

            if not cat_escolhida:
                print("Categoria inválida.")
                return

            forma = input("Forma de pagamento (dinheiro/debito/credito/pix): ")
            desc = input("Descrição: ")


            nova = cls(valor, dt, cat_escolhida, desc, forma)
            cls.salvar_despesas()
            
            from .orcamento_mensal import OrcamentoMensal
            OrcamentoMensal.gerar_orcamento(dt.month, dt.year)
            
            print("Despesa salva! Orçamento atualizado e alertas verificados.")

        except ValueError as e:
            print(f"Erro: {e}")

    @classmethod
    def editar_despesas(cls):
        Categoria.carregar_categorias()
        cls.carregar_despesas()

        if not cls.lista_despesas:
            print("Nenhuma despesa cadastrada.")
            return

        print("\nDespesas cadastradas:")
        for d in cls.lista_despesas:
            print(f"ID: {d.id} | Valor: {d.valor} | Data: {d.data} | Categoria: {d.categoria.nome} | Pagamento: {d.forma_pagamento}")

        try:
            id_escolhido = int(input("\nDigite o ID da despesa que deseja editar: "))
        except ValueError:
            print("ID inválido.")
            return

        despesa = next((d for d in cls.lista_despesas if d.id == id_escolhido), None)

        if despesa is None:
            print("Despesa não encontrada.")
            return
        while True:
            print("\nO que deseja editar?")
            print("1 - Valor")
            print("2 - Data")
            print("3 - Categoria")
            print("4 - Descrição")
            print("5 - Forma de pagamento")
            print("0 - Concluir edição")

            opcao = input("Escolha: ")

            try:
                if opcao == "1":
                    novo = float(input("Novo valor: "))
                    despesa.valor = novo

                elif opcao == "2":
                    nova_data = input("Nova data (AAAA-MM-DD): ")
                    despesa.data = datetime.date.fromisoformat(nova_data)

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

                    if nova_cat.tipo != "despesa":
                        print("Categoria escolhida não é do tipo despesa!")
                        continue

                    despesa.categoria = nova_cat

                elif opcao == "4":
                    novo = input("Nova descrição: ")
                    despesa.descricao = novo

                elif opcao == "5":
                    novo = input("Nova forma de pagamento (dinheiro/debito/credito/pix): ")
                    despesa.forma_pagamento = novo
                
                elif opcao == "0":
                    break

                else:
                    print("Opção inválida.")
                    return

            except Exception as e:
                print("Erro ao editar:", e)
                continue

        cls.salvar_despesas()
        print("\nDespesa atualizada com sucesso!")