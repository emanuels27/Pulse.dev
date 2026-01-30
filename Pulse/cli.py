import click
from pulse.analyzer import analyze_project

@click.group()
def cli():
    """Pulse.dev - Diagnóstico da saúde do código."""
    pass

@cli.command()
@click.argument("path", type=click.Path(exists=True))
def analyze(path):
    """Analisa um projeto Python."""
    analyze_project(path)
