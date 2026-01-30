# Pulse.dev ⚡

> Análise rápida da saúde de projetos direto pelo terminal.

**Pulse.dev** é uma ferramenta CLI em Python que analisa projetos locais e entrega
estatísticas claras sobre estrutura, arquivos e código Python — tudo em segundos.

Projeto open-source 🇧🇷 focado em produtividade, aprendizado e automação.

---

## ✨ O que é o Pulse.dev?

Pulse.dev nasceu como um projeto prático para:
- aprender Python de verdade
- criar uma CLI profissional
- gerar valor real para outros devs
- construir um projeto open-source do zero

Ele escaneia qualquer pasta de projeto e mostra:
- estrutura geral
- volume de arquivos
- tamanho do projeto
- métricas específicas de código Python

Tudo direto pelo terminal, sem dependências pesadas.

---

## 🚀 Features

- 📊 Análise geral da estrutura do projeto
- 🐍 Análise focada em projetos Python
- ⚡ Execução rápida
- 🧩 CLI simples e profissional
- 🤖 Saída em JSON para automação
- 📄 Modo resumido para README e relatórios
- 🔧 Fácil de estender
- 🇧🇷 Open-source feito no Brasil

---

## 📦 Instalação

### Requisitos
- Python 3.8 ou superior

### Instalação em modo desenvolvimento
```bash
git clone https://github.com/emanuels27/Pulse.dev.git
cd Pulse.dev
pip install -e .


📊 Uso
🔍 Análise geral do projeto
Copiar código
Bash
pulse scan .
Mostra:
número de pastas
número de arquivos
tamanho total
extensões mais comuns


🐍 Análise focada em Python
Copiar código
Bash
pulse python .
Mostra:
arquivos .py
linhas de código
funções
classes


⚡ Modos especiais
📄 Saída curta (--short)
Ideal para README, prints e relatórios rápidos.
Copiar código
Bash
pulse scan . --short
pulse python . --short
Exemplo:
Copiar código
Text
🐍 Pulse.dev — Análise Python

📄 Arquivos .py: 4
📏 Linhas de código: 137
🤖 Saída em JSON (--json)
Perfeita para automação, scripts e CI/CD.
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


🧠 Casos de uso reais
Avaliar rapidamente o tamanho de um projeto
Ter uma noção da complexidade de código Python
Automatizar métricas em pipelines
Gerar relatórios simples
Aprender como CLIs em Python funcionam na prática


📂 Estrutura do projeto
Copiar código
Text
pulse.dev/
├── pulse/
│   ├── __init__.py
│   ├── analyzer.py
│   └── cli.py
│
├── tests/
│   └── test_analyzer.py
│
├── pyproject.toml
├── README.md
└── .gitignore


🧭 Roadmap
[ ] Exportar relatório para arquivo
[ ] Suporte a mais linguagens
[ ] Métricas de complexidade
[ ] Integração com CI (GitHub Actions)
[ ] Sistema de plugins
[ ] Comparação entre projetos


🤝 Contribuindo
Contribuições são muito bem-vindas.
Faça um fork do projeto
Crie uma branch (feat/nova-feature)
Commit suas mudanças
Abra um Pull Request
Mesmo ideias simples já ajudam bastante.


📝 Licença
Este projeto está licenciado sob a licença MIT.


⭐ Apoie o projeto
Se o Pulse.dev te ajudou de alguma forma:
deixe uma ⭐ no repositório
compartilhe com outros devs
use como base para aprender Python e CLI
Feito com ❤️ no Brasil 🇧🇷
