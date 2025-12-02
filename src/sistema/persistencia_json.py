import json
import os
from datetime import date
from classes.categoria import Categoria
from classes.lancamento import Lancamento
from classes.despesa import Despesa
from classes.receita import Receita
from classes.alerta import Alerta


NOME_JSON = "lancamentos.json" 

def salvar_lancamentos_json(lista_lancamentos):
    """Serializa e salva no arquivo JSON."""
    dados_para_salvar = [lancamento.to_dict() for lancamento in lista_lancamentos]
    caminho_arquivo = os.path.join("data", NOME_JSON)
    
    try:
        os.makedirs("data", exist_ok=True)
        with open(caminho_arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados_para_salvar, f, indent=4)
        print(f"Dados salvos com sucesso em {caminho_arquivo}.")
    except Exception as e:
        print(f" Erro ao salvar dados: {e}")

def carregar_lancamentos_json():
    """Carrega dados do JSON e os transforma de volta em objetos Python."""
    caminho_arquivo = os.path.join("data", NOME_JSON)
    
    if not os.path.exists(caminho_arquivo):
        print(f"Arquivo {caminho_arquivo} não encontrado. Iniciando com lista vazia.")

        Lancamento.proximo_id = 1 
        return []

    lista_lancamentos = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            dados_carregados = json.load(f)
            
            if dados_carregados:
                ultimo_id = max(d.get("id", 0) for d in dados_carregados) 
                Lancamento.proximo_id = ultimo_id + 1
            
            for dados_lancamento in dados_carregados:

                cat_dict = dados_lancamento["categoria"]
                categoria_obj = Categoria(
                    nome=cat_dict["nome"], tipo=cat_dict["tipo"],
                    limite=cat_dict["limite"], descricao=cat_dict["descricao"]
                )
                
                data_obj = date.fromisoformat(dados_lancamento["data"])
                
                TipoLancamento = Despesa if cat_dict["tipo"] == "despesa" else Receita
                             
                lancamento_obj = TipoLancamento(
                    valor=dados_lancamento["valor"], data=data_obj,
                    categoria=categoria_obj, descricao=dados_lancamento["descricao"],
                    id=dados_lancamento["id"] 
                )
                lista_lancamentos.append(lancamento_obj)

        print(f"Dados carregados: {len(lista_lancamentos)} lançamentos encontrados. Próximo ID: {Lancamento.proximo_id}.")
        return lista_lancamentos

    except Exception as e:
        print(f"Erro ao carregar/processar dados: {e}")
        return []
    
