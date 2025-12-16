import json
CAMINHO_CATEGORIA = "data/categorias.json"

class Categoria:

    lista_categoria = []

    def __init__(self, nome, tipo, limite, descricao, id=None):
        nome = nome.strip()
        tipo = tipo.lower()
        for cat in Categoria.lista_categoria:
            if cat.nome.lower() == nome.lower() and cat.tipo == tipo:
                raise ValueError(f"A categoria '{nome}' já existe para o tipo {tipo}.")
        if tipo == "receita" and (limite is not None and limite > 0):
            raise ValueError("Categorias de receita não podem ter um limite de gastos.")
        if id is None:
            self.id = self.criar_proximo_id()
        else:
            self.id = id

        self.nome = nome
        self.tipo = tipo
        self.limite = limite
        self.descricao = descricao

        Categoria.lista_categoria.append(self)

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        if not valor or valor.strip() == "":
            raise ValueError("Nome Inválido.")
        self._nome = valor
        
    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, valor):
        tipos = ["despesa", "receita"]
        if not valor or valor.strip() == "":
            raise ValueError("Tipo inválido")
        valor = valor.lower()
        if valor not in tipos:
            raise ValueError("Tipo inválido")

        self._tipo = valor
        if valor == "receita":
            self._limite = None  

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, valor):

        if self.tipo == "receita":
            self._limite = 0.0
            return

        if valor is None:
            raise ValueError("Despesa deve ter limite")
        
        if not isinstance(valor, (int, float)):
            raise TypeError("Limite deve ser número.")
        
        if valor <= 0:
            raise ValueError("O limite deve ser maior que zero.")
        
        self._limite = valor

    @property
    def descricao(self):
        return self._descricao
    
    @descricao.setter
    def descricao(self, valor):
        if not valor or valor.strip() == "":
            raise ValueError("Categoria sem descrição")
        self._descricao = valor

    def __str__(self):
        return f"{self.nome}, {self.tipo}, {self.limite}, {self.descricao}, ID: {self.id}"

    def __eq__(self, outro):
        if not isinstance(outro, Categoria):
           return NotImplemented
        return self.id == outro.id
    
    def to_dict(self):
        return {
            "nome": self.nome,
            "tipo": self.tipo,
            "limite": self.limite,
            "descricao": self.descricao,
            "id": self.id
        }
    
    @classmethod
    def salvar_categorias(cls):
        with open(CAMINHO_CATEGORIA, "w", encoding="utf-8") as arq:
            json.dump([c.to_dict() for c in cls.lista_categoria],
                      arq, indent=4, ensure_ascii=False)
    
    @classmethod
    def carregar_categorias(cls):
        cls.lista_categoria.clear()
        try:
            with open(CAMINHO_CATEGORIA, "r", encoding="utf-8") as arq:
                dados = json.load(arq)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
        
        for item in dados:
            Categoria(
                nome=item["nome"],
                tipo=item["tipo"],
                limite=item["limite"],
                descricao=item["descricao"],
                id=item["id"]
            )
        return cls.lista_categoria
    
    @classmethod
    def criar_proximo_id(cls):
        try:
            with open(CAMINHO_CATEGORIA, "r", encoding="utf-8") as arq:
                ids = json.load(arq)
        except (FileNotFoundError, json.JSONDecodeError):
            return 1
        
        if not ids:
            return 1
        
        maior_id = max(item["id"] for item in ids)
        return maior_id + 1 
    
    @classmethod
    def criar_categoria(cls):
        cls.carregar_categorias()
        nome = str(input("Digite o nome da Categoria: ")).strip()
        tipo = str(input("Digite o tipo da Categoria (receita/despesa): ")).lower()
        
        if any(c.nome.lower() == nome.lower() and c.tipo == tipo for c in cls.lista_categoria):
            print(f"Erro: Já existe uma categoria de {tipo} com o nome '{nome}'.")
            return

        limite = None
        if tipo == "despesa": 
            limite = float(input("Digite o limite mensal da categoria: "))
            
        descricao = str(input("Digite a descrição: "))
        cls(nome, tipo, limite, descricao)
        cls.salvar_categorias()
        print(f"Categoria '{nome}' salva com sucesso!")

    @classmethod
    def excluir_categoria(cls):
        cls.carregar_categorias()
        if not cls.lista_categoria:
            print("Nenhuma categoria para excluir.")
            return

        for c in cls.lista_categoria: print(f"ID: {c.id} | {c.nome} ({c.tipo})")
        
        try:
            id_exc = int(input("\nID da categoria para excluir: "))
            cat = next((c for c in cls.lista_categoria if c.id == id_exc), None)
            
            if cat:
                cls.lista_categoria.remove(cat)
                cls.salvar_categorias()
                print("Categoria excluída com sucesso!")
            else:
                print("ID não encontrado.")
        except ValueError:
            print("ID inválido.")

    @classmethod
    def editar_categorias(cls):

        cls.carregar_categorias()

        if not cls.lista_categoria:
            print("Nenhuma categoria cadastrada.")
            return

        print("\nCategorias disponíveis:")
        for cat in cls.lista_categoria:
            print(
                f"ID: {cat.id} | Nome: {cat.nome} | Tipo: {cat.tipo} | Limite: {cat.limite}"
            )

        try:
            id_escolhido = int(input("\nDigite o ID da categoria que deseja editar: "))
        except ValueError:
            print("ID inválido.")
            return

        categoria = next((c for c in cls.lista_categoria if c.id == id_escolhido), None)

        if categoria is None:
            print("Categoria não encontrada.")
            return

        while True:
            print("\nO que deseja editar?")
            print("1 - Nome")
            print("2 - Tipo")
            print("3 - Limite")
            print("4 - Descrição")
            print("0 - Concluir")

            opcao = input("Escolha: ")

            try:
                if opcao == "1":
                    categoria.nome = input("Novo nome: ")

                elif opcao == "2":
                    categoria.tipo = input("Novo tipo (despesa/receita): ")

                elif opcao == "3":
                    if categoria.tipo == "receita":
                        print("Receitas não possuem limite. Definido como None.")
                        categoria.limite = None
                    else:
                        categoria.limite = float(input("Novo limite: "))

                elif opcao == "4":
                    categoria.descricao = input("Nova descrição: ")

                elif opcao == "0":
                    break

                else:
                    print("Opção inválida.")
                    continue

            except Exception as e:
                print("Erro ao editar:", e)
                continue

        cls.salvar_categorias()
        print("\nCategoria atualizada com sucesso!")
