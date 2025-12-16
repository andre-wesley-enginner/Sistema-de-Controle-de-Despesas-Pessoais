from abc import ABC, abstractmethod

# --- O PADRÃO STRATEGY ---

# 1. A Interface (Classe Abstrata)
class EstrategiaExportacao(ABC):
    @abstractmethod
    def exportar(self, relatorio):
        pass

# 2. Estratégia concreta: Exibição no Terminal (CLI)
class ExportarConsole(EstrategiaExportacao):
    def exportar(self, r):
        print(f"\n" + "="*40)
        print(f"{f'RELATÓRIO ANALÍTICO {r.mes}/{r.ano}':^40}")
        print("="*40)
        print(f"Receitas Totais:  R$ {r.total_receitas:>10.2f}")
        print(f"Despesas Totais:  R$ {r.total_despesas:>10.2f}")
        print(f"Saldo Final:      R$ {r.saldo:>10.2f}")
        print("-" * 40)

        if r.orcamento_anterior:
            dif = r.saldo - r.orcamento_anterior.saldo
            status = "MELHOR" if dif >= 0 else "PIOR"
            print(f"Desempenho: R$ {abs(dif):.2f} {status} que o mês anterior.")

        print("\nDISTRIBUIÇÃO POR CATEGORIA (Top Gastos):")
        categorias_ordenadas = sorted(
            r.gastos_por_categoria.items(), 
            key=lambda x: x[1]['gasto'], 
            reverse=True
        )

        for nome, dados in categorias_ordenadas:
            percentual = (dados['gasto'] / r.total_despesas * 100) if r.total_despesas > 0 else 0
            print(f"- {nome:<15}: R$ {dados['gasto']:>8.2f} ({percentual:>5.1f}%)")
            if dados.get('limite', 0) > 0 and dados['gasto'] > dados['limite']:
                print(f"  [ALERTA: LIMITE EXCEDIDO! Limite: R$ {dados['limite']:.2f}]")
        
        if len(categorias_ordenadas) > 0:
            media = r.total_despesas / len(categorias_ordenadas)
            print(f"\nMédia de gasto por categoria: R$ {media:.2f}")
        print("="*40)

# 3. Estratégia concreta: Guardar em Ficheiro TXT
class ExportarTXT(EstrategiaExportacao):
    def exportar(self, r):
        nome_arq = f"relatorio_{r.mes}_{r.ano}.txt"
        with open(nome_arq, "w", encoding="utf-8") as f:
            f.write(f"RELATÓRIO FINANCEIRO - {r.mes}/{r.ano}\n")
            f.write("="*30 + "\n")
            f.write(f"Receitas: R$ {r.total_receitas:.2f}\n")
            f.write(f"Despesas: R$ {r.total_despesas:.2f}\n")
            f.write(f"Saldo:    R$ {r.saldo:.2f}\n")
        print(f"\n[SUCESSO] Relatório exportado para {nome_arq}")

# --- A CLASSE CONTEXTO (RELATÓRIO) ---

class Relatorio:
    def __init__(self, mes, ano, total_despesas, total_receitas, saldo, gastos_por_categoria, orcamento_anterior=None):
        self.mes = mes
        self.ano = ano
        self.total_despesas = total_despesas
        self.total_receitas = total_receitas
        self.saldo = saldo
        self.gastos_por_categoria = gastos_por_categoria
        self.orcamento_anterior = orcamento_anterior

    @classmethod
    def gerar_relatorio_mensal(cls, mes, ano):
        from .orcamento_mensal import OrcamentoMensal

        OrcamentoMensal.carregar_orcamentos()
        orcamento = OrcamentoMensal.gerar_orcamento(mes, ano)
        
        mes_ant = 12 if mes == 1 else mes - 1
        ano_ant = ano - 1 if mes == 1 else ano
        
        orcamento_anterior = next(
            (o for o in OrcamentoMensal.lista_orcamentos if o.mes == mes_ant and o.ano == ano_ant), 
            None
        )

        return cls(mes, ano, orcamento.total_despesas, orcamento.total_receitas, 
                   orcamento.saldo, orcamento.orcamento_por_categoria, orcamento_anterior)

    def exibir(self, estrategia: EstrategiaExportacao = None):
        if estrategia is None:
            estrategia = ExportarConsole()
        estrategia.exportar(self)

    @staticmethod
    def calcular_percentual(gasto, limite):
        if limite <= 0: return 0
        return (gasto / limite) * 100