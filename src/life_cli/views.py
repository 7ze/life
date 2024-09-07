import time

from blessed import Terminal

from life_cli.grid import Grid
from life_cli.patterns import Pattern

term = Terminal()

PADDING_TOP = 1
PADDING_BOTTOM = 1

__all__ = ["CLIView"]


class CLIView:
    def __init__(self, pattern: Pattern, gen=20, frame_rate=7, size=17) -> None:
        self.pattern = pattern
        self.gen = gen
        self.frame_rate = frame_rate
        self.size = size

    def display_top_panel(self) -> None:
        top_panel = 1 + PADDING_TOP
        title_text = f"{term.green}Game of Life{term.normal}: {term.italic}{self.pattern.name}{term.normal}"
        print(term.move_y(top_panel) + term.center(title_text))
        print("⎯" * term.width)

    def display_bottom_panel(self) -> None:
        bottom_panel = term.height - PADDING_BOTTOM
        help_instructions = f"{term.italic}Keys Info{term.normal}: {term.red}[q] Quit / Skip{term.normal}"
        print(term.move_y(bottom_panel) + term.center(help_instructions))

    def display_grid(self) -> None:
        grid_panel = term.height // 2 - self.size // 2 - 1
        print(term.move_y(grid_panel))
        grid = Grid(self.pattern)
        for _ in range(self.gen):
            for row in grid.as_string(self.size).split("\n"):
                print(term.center(row))
            time.sleep(1 / self.frame_rate)
            grid.evolve()
            print(term.move_y(grid_panel) + term.clear_eol)
            key = term.inkey(timeout=0.01)
            if key == "q":
                break

    def draw(self) -> None:
        with term.fullscreen(), term.hidden_cursor(), term.cbreak():
            self.display_top_panel()
            self.display_bottom_panel()
            self.display_grid()
