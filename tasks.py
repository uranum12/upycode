from pathlib import Path

from invoke.context import Context
from invoke.tasks import task

src = " ".join(
    str(f)
    for p in Path.cwd().iterdir()
    if not p.name.startswith(".")
    for f in p.rglob("*.py")
)


@task
def fmt(c: Context) -> None:
    """format source files"""
    c.run(f"ruff format {src}", pty=True)
    c.run(f"ruff check --fix-only --show-fixes {src}", pty=True)


@task
def lint(c: Context) -> None:
    """check source files"""
    c.run(f"ruff format --check {src}", pty=True)
    c.run(f"ruff check {src}", pty=True)
