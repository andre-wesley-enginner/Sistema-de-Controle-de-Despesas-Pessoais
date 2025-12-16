import sys
from datetime import date
from classes.categoria import Categoria
from classes.receita import Receita
from classes.despesa import Despesa
from classes.relatorio import Relatorio, ExportarConsole, ExportarTXT
from classes.alerta import Alerta
from classes.orcamento_mensal import OrcamentoMensal

def inicializar_sistema():
    """Carrega todos os dados dos arquivos JSON ao iniciar."""
    Categoria.carregar_categorias()
    Receita.carregar_receitas()
    Despesa.carregar_despesas()
    Alerta.carregar_alertas()
    OrcamentoMensal.carregar_orcamentos()

def menu_principal():
    print("\n" + "="*50)
    print(f"{'SISTEMA DE CONTROLE FINANCEIRO':^50}")
    print("="*50)
    print("1. Gerenciar Categorias (Receita/Despesa)")
    print("2. Lançamentos (Receitas e Despesas)")
    print("3. Orçamentos e Alertas")
    print("4. Relatórios Analíticos")
    print("0. Sair")
    print("-" * 50)
    return input("Escolha uma opção: ")

# --- SUBMENUS ---

def submenu_categorias():
    while True:
        print("\n[CATEGORIAS] 1. Criar | 2. Editar | 3. Listar | 4. Excluir | 0. Voltar")
        op = input("Opção: ")
        if op == "1": Categoria.criar_categoria()
        elif op == "2": Categoria.editar_categorias()
        elif op == "3":
            for c in Categoria.lista_categoria: print(c)
        elif op == "4": Categoria.excluir_categoria()
        elif op == "0": break

def submenu_lancamentos():
    while True:
        print("\n[LANÇAMENTOS] 1. Nova Receita | 2. Nova Despesa | 3. Editar | 0. Voltar")
        op = input("Opção: ")
        if op == "1": Receita.criar_receita()
        elif op == "2": Despesa.criar_despesa()
        elif op == "3":
            sub = input("Editar: 1. Receita | 2. Despesa: ")
            if sub == "1": Receita.editar_receitas()
            else: Despesa.editar_despesas()
        elif op == "0": break

def submenu_orcamentos_alertas():
    while True:
        print("\n[ORÇAMENTOS/ALERTAS] 1. Gerar Orçamento Mensal | 2. Ver Alertas | 0. Voltar")
        op = input("Opção: ")
        if op == "1":
            m = int(input("Mês: ")); a = int(input("Ano: "))
            orc = OrcamentoMensal.gerar_orcamento(m, a)
            print(orc)
        elif op == "2":
            alertas = Alerta.carregar_alertas()
            if not alertas: print("Nenhum alerta registrado.")
            for al in alertas: print(al)
        elif op == "0": break

# --- EXECUÇÃO ---

def executar_cli():
    inicializar_sistema()
    while True:
        opcao = menu_principal()
        if opcao == "1": submenu_categorias()
        elif opcao == "2": submenu_lancamentos()
        elif opcao == "3": submenu_orcamentos_alertas()
        elif opcao == "4":
            try:
                m = int(input("Mês: "))
                a = int(input("Ano: "))
                rel = Relatorio.gerar_relatorio_mensal(m, a)
                
                print("\nComo deseja visualizar?")
                print("1. Ver no Terminal")
                print("2. Exportar para ficheiro .txt")
                tipo = input("Escolha: ")
                
                if tipo == "2":
                    rel.exibir(ExportarTXT())
                else:
                    rel.exibir(ExportarConsole()) # Usa a estratégia padrão
                    
            except Exception as e: 
                print(f"Erro ao gerar relatório: {e}")
        elif opcao == "0":
            print("\nSalvando dados...")
            try:
                # Chama os métodos de salvamento de cada classe
                Categoria.salvar_categorias()
                Receita.salvar_receitas()
                Despesa.salvar_despesas()
                Alerta.salvar_alertas()
                OrcamentoMensal.salvar_orcamentos()
                
                print("Dados salvos com sucesso!")
                print("Encerrando sistema. Até logo!")
            except Exception as e:
                print(f"Erro ao salvar dados: {e}")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    inicializar_sistema()