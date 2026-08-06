from __future__ import annotations

import ast
import importlib
import io
import sys
from contextlib import redirect_stdout
from pathlib import Path
from types import ModuleType
from typing import Any, Iterable
from unittest.mock import MagicMock, patch

ROOT = Path(__file__).resolve().parents[1]

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def purge_modules(*prefixes: str) -> None:
    """Remove modules and their children so import-time behavior can be retested."""
    for name in list(sys.modules):
        if any(name == prefix or name.startswith(prefix + ".") for prefix in prefixes):
            sys.modules.pop(name, None)


def load_apc_functions_with_fake_database():
    """Import APC_Functions without opening or changing the real project database."""
    purge_modules("Classes_and_Objects.APC_Functions", "Classes_and_Objects.APC_Classes_Objects")

    fake_cursor = MagicMock(name="bootstrap_cursor")
    # Long enough for both six-column moon rows and ten-column planet rows.
    fake_cursor.fetchone.return_value = (
        "Test Body", 1.0, 2.0, 3.0, None, "Test Parent", 6.0, 7.0, 8, 9.0
    )
    fake_connection = MagicMock(name="bootstrap_connection")
    fake_connection.cursor.return_value = fake_cursor

    with patch("sqlite3.connect", return_value=fake_connection), redirect_stdout(io.StringIO()):
        module = importlib.import_module("Classes_and_Objects.APC_Functions")

    return module


def load_classes_with_fake_database():
    """Import APC_Classes_Objects without opening or changing the real database."""
    purge_modules("Classes_and_Objects.APC_Classes_Objects")

    fake_cursor = MagicMock(name="bootstrap_cursor")
    fake_cursor.fetchone.return_value = (
        "Test Body", 1.0, 2.0, 3.0, None, "Test Parent", 6.0, 7.0, 8, 9.0
    )
    fake_connection = MagicMock(name="bootstrap_connection")
    fake_connection.cursor.return_value = fake_cursor

    with patch("sqlite3.connect", return_value=fake_connection), redirect_stdout(io.StringIO()):
        module = importlib.import_module("Classes_and_Objects.APC_Classes_Objects")

    return module


def load_ast_definitions(
    source_path: Path,
    names: Iterable[str],
    namespace: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Load selected classes/functions without executing a GUI module's top-level code."""
    source = source_path.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(source_path))
    wanted = set(names)
    selected = [
        node
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))
        and node.name in wanted
    ]
    missing = wanted.difference(node.name for node in selected)
    if missing:
        raise AssertionError(f"Definitions not found in {source_path}: {sorted(missing)}")

    module = ast.Module(body=selected, type_ignores=[])
    ast.fix_missing_locations(module)
    env: dict[str, Any] = {"__builtins__": __builtins__}
    if namespace:
        env.update(namespace)
    exec(compile(module, str(source_path), "exec"), env)
    return env


def has_top_level_call(source_path: Path, call_names: set[str]) -> bool:
    """Return True when a named function is called directly at module scope."""
    tree = ast.parse(source_path.read_text(encoding="utf-8"), filename=str(source_path))
    found = False

    class TopLevelCallVisitor(ast.NodeVisitor):
        def visit_FunctionDef(self, node):  # Do not descend into definitions.
            return None

        def visit_AsyncFunctionDef(self, node):
            return None

        def visit_ClassDef(self, node):
            return None

        def visit_Call(self, node):
            nonlocal found
            func = node.func
            if isinstance(func, ast.Name):
                name = func.id
            elif isinstance(func, ast.Attribute):
                name = func.attr
            else:
                name = None
            if name in call_names:
                found = True
            self.generic_visit(node)

    visitor = TopLevelCallVisitor()
    for node in tree.body:
        visitor.visit(node)
    return found


class FakeRawTurtle:
    """Small turtle replacement used to test coordinate calculations headlessly."""

    def __init__(self, screen=None, shape=None):
        self.screen = screen
        self.shape_name = shape
        self.goto_calls: list[tuple[float, float]] = []
        self.current_color = None

    def color(self, value):
        self.current_color = value

    def up(self):
        pass

    def pd(self):
        pass

    def penup(self):
        pass

    def pendown(self):
        pass

    def goto(self, x, y):
        self.goto_calls.append((x, y))


class FakeTurtleModule(ModuleType):
    RawTurtle = FakeRawTurtle
