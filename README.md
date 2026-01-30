# Pulse.dev ⚡

**Pulse.dev** é uma ferramenta de linha de comando (CLI) escrita em **Python** para analisar rapidamente a estrutura de projetos de código.

Ela mostra métricas como:
- quantidade de pastas e arquivos
- tamanho total do projeto
- extensões mais usadas
- métricas específicas de código Python (linhas, funções, classes)

Ideal para:
- desenvolvedores
- estudantes
- análise rápida de repositórios
- automações e scripts

---

## 🚀 Instalação (modo desenvolvimento)

Clone o repositório:

```bash
git clone git@github.com:emanuels27/Pulse.dev.git
cd Pulse.dev
Instale em modo editável:
Copiar código
Bash
pip install -e .
🧠 Como usar
📊 Análise geral do projeto
Copiar código
Bash
pulse scan .
Saída exemplo:
Copiar código

📊 Pulse.dev — Análise do Projeto

📁 Pastas: 68
📄 Arquivos: 103
💾 Tamanho total: 59.55 KB

🔝 Extensões mais comuns:
  .py: 4
  .txt: 5
  .sample: 14

🐍 Análise específica de Python
Copiar código
Bash
pulse python .
Saída exemplo:
Copiar código

🐍 Pulse.dev — Análise Python

📄 Arquivos .py: 4
📏 Linhas de código: 137
🧠 Funções: 6
🏛️ Classes: 0
⚡ Modos rápidos
Versão curta (short)
Copiar código
Bash
pulse scan . --short
pulse python . --short
📦 Saída em JSON (ideal para automações)
Copiar código
Bash
pulse scan . --json
pulse python . --json
Exemplo:
Copiar código
Json
{
  "files": 4,
  "lines": 137,
  "functions": 6,
  "classes": 0
}
🧱 Estrutura do projeto
Copiar código

pulse/
├── analyzer.py   # Lógica de análise
├── cli.py        # Interface de linha de comando
└── __init__.py
tests/
pyproject.toml
README.md

🎯 Objetivo do projeto
O Pulse.dev nasceu com foco em:
aprendizado prático de Python
construção de uma CLI real
projeto open source acessível para a comunidade BR

🛠️ Tecnologias
Python 3.10+
argparse
pathlib
Git + GitHub
Termux friendly ✅

📌 Status
🚧 v0.1.0 — versão inicial funcional
Próximos passos:
suporte a mais linguagens
métricas por pasta
gráficos
integração CI

🤝 Contribuição
Pull requests são bem-vindos.
Ideias, issues e sugestões também!

📄 Licença
MIT License
