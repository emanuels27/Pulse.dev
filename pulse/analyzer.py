from pathlib import Path

def analyze_project(path: str):
    project_path = Path(path)
    python_files = list(project_path.rglob("*.py"))

    print("📂 Projeto analisado:", project_path.name)
    print("🐍 Arquivos Python encontrados:", len(python_files))
