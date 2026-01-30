import argparse
import json
from pulse.analyzer import analyze_project, analyze_python


def run_scan(path, as_json=False, short=False):
    result = analyze_project(path)

    if as_json:
        print(json.dumps(result, indent=2))
        return

    print("\n📊 Pulse.dev — Análise do Projeto\n")

    print(f"📁 Pastas: {result['folders']}")
    print(f"📄 Arquivos: {result['files']}")
    print(f"💾 Tamanho total: {result['size_kb']:.2f} KB")

    if short:
        return

    print("\n🔝 Extensões mais comuns:")
    for ext, count in result["extensions"]:
        print(f"  {ext}: {count}")


def run_python(path, as_json=False, short=False):
    py = analyze_python(path)

    if as_json:
        print(json.dumps(py, indent=2))
        return

    print("\n🐍 Pulse.dev — Análise Python\n")

    print(f"📄 Arquivos .py: {py['files']}")
    print(f"📏 Linhas de código: {py['lines']}")

    if short:
        return

    print(f"🧠 Funções: {py['functions']}")
    print(f"🏛️ Classes: {py['classes']}")


def main():
    parser = argparse.ArgumentParser(
        description="📊 Pulse.dev — Analisador de projetos"
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    scan = subparsers.add_parser("scan", help="Analisa o projeto")
    scan.add_argument("path", nargs="?", default=".")
    scan.add_argument("--json", action="store_true")
    scan.add_argument("--short", action="store_true")

    python = subparsers.add_parser("python", help="Análise focada em Python")
    python.add_argument("path", nargs="?", default=".")
    python.add_argument("--json", action="store_true")
    python.add_argument("--short", action="store_true")

    args = parser.parse_args()

    if args.command == "scan":
        run_scan(args.path, args.json, args.short)
    elif args.command == "python":
        run_python(args.path, args.json, args.short)


if __name__ == "__main__":
    main()
