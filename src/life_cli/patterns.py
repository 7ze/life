from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import tomllib

PATTERNS_FILE = Path(__file__).parent / "patterns.toml"

type patterns = dict[str, dict[str, list[list[int]]]]
type pattern = dict[str, list[list[int]]]


@dataclass
class Pattern:
    name: str
    alive_cells: set[tuple[int, int]]

    @classmethod
    def new(cls, name: str, pattern: pattern) -> Pattern:
        # The cell is always a list of two integers (x, y), but the type checker
        # can't infer this.
        # Ignoring type check because the tuple conversion is safe.
        return cls(
            name,
            {tuple(cell) for cell in pattern["alive_cells"]},  # type: ignore
        )


def get_pattern(name: str, filename=PATTERNS_FILE) -> Pattern:
    data: patterns = tomllib.loads(filename.read_text(encoding="utf-8"))
    return Pattern.new(name, data[name])


def get_patterns(filename=PATTERNS_FILE) -> list[Pattern]:
    data: patterns = tomllib.loads(filename.read_text(encoding="utf-8"))
    return [Pattern.new(name, pattern) for name, pattern in data.items()]
