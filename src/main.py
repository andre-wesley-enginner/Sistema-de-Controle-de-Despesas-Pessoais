import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from sistema.CLI import executar_cli

def main():
    """Ponto de entrada único para o Sistema de Controle Financeiro."""
    try:
        executar_cli()
    except KeyboardInterrupt:
        print("\nSistema encerrado pelo usuário.")
    except Exception as e:
        print(f"Ocorreu um erro crítico: {e}")

if __name__ == "__main__":
    main()