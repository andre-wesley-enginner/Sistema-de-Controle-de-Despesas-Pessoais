from .lancamento import Lancamento
import json
from .categoria import Categoria
import datetime
CAMINHO_RECEITA = "data/receitas.json"

class Receita(Lancamento):
    lista_receitas = []
    def __init__(self, valor, data, categoria, descricao, forma_recebimento, id=None):
        super().__init__(valor, data, categoria, descricao, id=id)
        self.forma_recebimento = forma_recebimento
        Receita.lista_receitas.append(self)

    @property
    def forma_recebimento(self):
        return self._forma_recebimento
    
    @forma_recebimento.setter
    def forma_recebimento(self, valor):
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
            self._forma_recebimento = valor  
        
    def __str__(self):
        return (f"Receita de {self.valor}, Categoria {self.categoria.nome}, data {self.data}, forma de recebimento {self.forma_recebimento}, descrição {self.descricao}")
    
    def __eq__(self, outro):
        if not isinstance(outro, Receita):
            return NotImplemented
        return self.id == outro.id
    
    def __repr__(self):
        return (f"valor={self.valor}, data={self.data}, Categoria={self.categoria}, forma de recebimento {self.forma_recebimento},  descrição={self.descricao}")
        
    def to_dict(self):
        d = super().to_dict()
        d["forma_recebimento"] = self.forma_recebimento
        return d
    
    @classmethod
    def salvar_receitas(cls):
        with open(CAMINHO_RECEITA, "w", encoding="utf-8") as arq:
            json.dump([receita.to_dict() for receita in cls.lista_receitas]
                      , arq, indent=4, ensure_ascii=False)
    
    @classmethod
    def carregar_receitas(cls):
        Categoria.carregar_categorias()
        cls.lista_receitas.clear()

        try:
            with open(CAMINHO_RECEITA, "r", encoding="utf-8") as arq:
                dados = json.load(arq)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

        for item in dados:
            cat = next((c for c in Categoria.lista_categoria 
                        if c.id == item["categoria"]["id"]), None)

            if cat is None:
                cat = Categoria(
                    nome=item["categoria"]["nome"],
                    tipo=item["categoria"]["tipo"],
                    limite=item["categoria"]["limite"],
                    descricao=item["categoria"]["descricao"],
                    id=item["categoria"]["id"]
                )

            Receita(
                valor=item["valor"],
                data=datetime.date.fromisoformat(item["data"]),
                categoria=cat,
                descricao=item["descricao"],
                forma_recebimento=item["forma_recebimento"],
                id=item["id"]
            )

        return cls.lista_receitas
    
    @classmethod
    def criar_receita(cls):
        # 1. Carrega os dados atuais do JSON para a memória primeiro
        cls.carregar_receitas()
        Categoria.carregar_categorias()

        try:
            valor = float(input("Valor da receita: "))
            data_str = input("Data (AAAA-MM-DD): ")
            dt = datetime.date.fromisoformat(data_str)
            
            # Filtrar apenas categorias de despesa
            categorias_receitas = [c for c in Categoria.lista_categoria if c.tipo == "receita"]
            if not categorias_receitas:
                print("Erro: Não existem categorias de receita cadastradas.")
                return

            print("\nCategorias de Receita:")
            for c in categorias_receitas:
                print(f"ID: {c.id} | Nome: {c.nome}")
            
            id_cat = int(input("Digite o ID da categoria: "))
            cat_escolhida = next((c for c in categorias_receitas if c.id == id_cat), None)

            if not cat_escolhida:
                print("ID de categoria inválido!")
                return

            desc = input("Descrição: ")
            forma = input("Forma de recebimento (dinheiro/debito/credito/pix): ")

            # 2. Instancia o objeto (o __init__ o adiciona na lista_despesas)
            cls(valor, dt, cat_escolhida, desc, forma)

            # 3. Salva no JSON
            cls.salvar_receitas()
            print("Receita lançada e salva com sucesso!")

        except ValueError as e:
            print(f"Erro nos dados digitados: {e}")

    @classmethod
    def editar_receitas(cls):
        Categoria.carregar_categorias()
        cls.carregar_receitas()

        if not cls.lista_receitas:
            print("Nenhuma receita cadastrada.")
            return

        print("\nReceitas cadastradas:")
        for r in cls.lista_receitas:
            print(f"ID: {r.id} | Valor: {r.valor} | Data: {r.data} | Categoria: {r.categoria.nome} | Recebimento: {r.forma_recebimento}")

        try:
            id_escolhido = int(input("\nDigite o ID da receita que deseja editar: "))
        except ValueError:
            print("ID inválido.")
            return

        receita = next((r for r in cls.lista_receitas if r.id == id_escolhido), None)

        if receita is None:
            print("Receita não encontrada.")
            return

        while True:
            print("\nO que deseja editar?")
            print("1 - Valor")
            print("2 - Data")
            print("3 - Categoria")
            print("4 - Descrição")
            print("5 - Forma de recebimento")
            print("0 - Concluir edição")

            opcao = input("Escolha: ")

            try:
                if opcao == "1":
                    novo = float(input("Novo valor: "))
                    receita.valor = novo

                elif opcao == "2":
                    nova_data = input("Nova data (AAAA-MM-DD): ")
                    receita.data = datetime.date.fromisoformat(nova_data)

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

                    if nova_cat.tipo != "receita":
                        print("Categoria escolhida não é do tipo receita!")
                        continue

                    receita.categoria = nova_cat

                elif opcao == "4":
                    novo = input("Nova descrição: ")
                    receita.descricao = novo

                elif opcao == "5":
                    novo = input("Nova forma de recebimento (dinheiro/debito/credito/pix): ")
                    receita.forma_recebimento = novo

                elif opcao == "0":
                    break

                else:
                    print("Opção inválida.")
                    continue

            except Exception as e:
                print("Erro ao editar:", e)
                continue

        cls.salvar_receitas()
        print("\nReceita atualizada com sucesso!")

    def verificar_categoria(self):
        if self.valor > 0 and self.categoria.tipo == "receita":
            print("Verificada")
            return True
        else:
            print("Item não é uma receita")
            return False