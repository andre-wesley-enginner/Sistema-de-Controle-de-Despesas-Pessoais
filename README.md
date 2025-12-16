# 💰 Sistema de Controle de Despesas Pessoais

[![Python Version](https://img.shields.io/badge/python-3.12%2B-blue)](https://www.python.org/)
[![POO-UFCA](https://img.shields.io/badge/POO-Semana%205-green)](https://github.com/andre-wesley-enginner/Sistema-de-Controle-de-Despesas-Pessoais)

Sistema robusto de gerenciamento financeiro desenvolvido em **Python**, focado na aplicação prática de **Programação Orientada a Objetos (POO)**. O projeto permite o controle total de fluxos de caixa, monitoramento de orçamentos e análise de dados através de relatórios extensíveis.

Este projeto foi desenvolvido como requisito final para a disciplina de POO da **Universidade Federal do Cariri (UFCA)**.

---

## 🏗️ Arquitetura e Design Patterns

O sistema foi projetado para ser modular e extensível, seguindo rigorosamente os princípios de POO. Para a entrega final (**Semana 5**), destaca-se a implementação do padrão **Strategy**, garantindo o cumprimento do princípio **Open/Closed** do SOLID.

### 📌 **Modelagem do Sistema (UML)**
O diagrama reflete a estrutura de herança entre lançamentos e a injeção de dependência no módulo de relatórios para diferentes formatos de exportação.

![Diagrama UML do Sistema](docs/UML_Sistema_Controle_Despesas.png)

### 🧩 **Destaques da Implementação Técnica**
* **Padrão Strategy**: Implementado na geração de relatórios. A interface `EstrategiaExportacao` permite que o sistema suporte múltiplos formatos (`ExportarConsole`, `ExportarTXT`) sem alteração no núcleo da classe `Relatorio`.
* **Abstração e Herança**: Utilização da classe base `Lancamento` para padronizar comportamentos de `Receita` e `Despesa`, aplicando polimorfismo em validações de saldo e limites.
* **Encapsulamento Avançado**: Uso rigoroso de atributos privados e decoradores `@property` para garantir a integridade dos dados financeiros.
* **Métodos Especiais (Dunder Methods)**: Sobrecarga de operadores como `__add__` (para soma de valores de objetos), `__eq__` (para comparação) e `__str__` para representação textual.

---

## ⚙️ Funcionalidades de Análise

O sistema transcende o registro básico, oferecendo **Relatórios Analíticos** reais:

* 📊 **Representatividade Percentual**: Cálculo do peso de cada categoria no orçamento total.
* 📈 **Comparativo Mensal**: Comparação automática com o mês anterior, indicando melhora ou piora no saldo.
* 🚨 **Alertas Inteligentes**: Notificações em tempo real sobre limites de categoria excedidos e déficits orçamentários.
* 💾 **Persistência Centralizada**: Gerenciamento de dados via arquivos JSON com salvamento automático.

---

## 📂 Organização do Projeto

A estrutura segue um padrão modular para facilitar a manutenção e escalabilidade:
```
sistema-controle-despesas/
│
├── src/
│   ├── main.py                     # Arquivo principal 
│   │
│   ├── classes/                    # Classes do Sistema   
│   │   ├── alerta.py               
│   │   ├── categoria.py            
│   │   ├── despesa.py              
│   │   ├── lancamento.py           
│   │   ├── orcamento_mensal.py     
│   │   ├── receita.py              
│   │   └── relatorio.py            
│   │
│   ├── sistema/                    # Núcleo do sistema
│   │   ├── CLI.py    
│
├── data/                           # Armazena arquivos de dados
│   ├── categorias.json
│   ├── lancamentos.json
│   ├── orcamentos.json
│   ├── receitas.json
│   ├── despesas.json
│   ├── relatorios.json
│   └── alertas.json
│
├── docs/                           # Documentação do projeto
│   └── UML_Sistema_Controle_Despesas.png
│
├── LICENSE                         # Licença do projeto
├── .gitignore                      # Arquivos ignorados no Git
│
└── README.md                       # Documentação geral do projeto
```

## 🔧 Como Iniciar

Siga os passos abaixo para configurar e executar o projeto em seu ambiente local:
### 1. Clonar o Repositório
```bash
git clone https://github.com/andre-wesley-enginner/Sistema-de-Controle-de-Despesas-Pessoais.git
cd Sistema-de-Controle-de-Despesas-Pessoais
```
### 2 Configurar o Ambiente

Certifique-se de ter o Python 3.12+ instalado. Recomenda-se o uso do Pytest para os testes:
```bash
pip install pytest
```
### 3 Executar a aplicação

Para iniciar o sistema via CLI, execute:
```bash
python src/main.py
```

## 🧪 Testes Automatizados

A integridade do sistema é garantida por uma suíte de 15 testes unitários. Eles validam regras de negócio críticas, como limites orçamentários e persistência.

Para rodar os testes, utilize o comando:
```bash
pytest
```

## 🎓 Informações Acadêmicas

* 🏛️ **Instituição**: Universidade Federal do Cariri (UFCA)

* 📚 **Disciplina**: Programação Orientada a Objetos

* 💻 **Projeto**: Tema 5 — Sistema de Controle de Despesas Pessoais

* 👨‍💻 **Autor**: André Wesley Barbosa Rodrigues Filho

* 🏷️ **Versão Final**: 1.0 (Tag v1.0)