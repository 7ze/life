from collections import defaultdict

from blessed import Terminal

from life_cli.patterns import Pattern

term = Terminal()

ALIVE = f"{term.blue}  {term.normal}"
DEAD = " . "


class Grid:
    def __init__(self, pattern: Pattern) -> None:
        self.pattern = pattern

    def __str__(self) -> str:
        return (
            f"{self.pattern.name}:\n"
            f"Alive cells -> {sorted(self.pattern.alive_cells)}"
        )

    def evolve(self) -> None:
        neighbours_delta = (
            (-1, 1),  # top left
            (0, 1),  # top
            (1, 1),  # top right
            (-1, 0),  # left
            (1, 0),  # right
            (-1, -1),  # bottom left
            (0, -1),  # bottom
            (1, -1),  # bottom right
        )

        num_neighbours = defaultdict(int)

        for row, col in self.pattern.alive_cells:
            for dr, dc in neighbours_delta:
                num_neighbours[(row + dr, col + dc)] += 1

        stay_alive = {
            cell for cell, num in num_neighbours.items() if num in {2, 3}
        } & self.pattern.alive_cells

        come_alive = {
            cell for cell, num in num_neighbours.items() if num == 3
        } - self.pattern.alive_cells

        self.pattern.alive_cells = stay_alive | come_alive

    def as_string(self, size: int) -> str:
        bounding_box = (0, 0, size, size)
        start_row, start_col, end_row, end_col = bounding_box
        display = []

        for col in range(start_col, end_col):
            display_row = [
                ALIVE if (row, col) in self.pattern.alive_cells else DEAD
                for row in range(start_row, end_row)
            ]
            display.append(" ".join(display_row))

        return "\n ".join(display)
