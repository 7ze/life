import argparse

from life_cli import patterns, views
from life_cli.version import __version__


def get_command_line_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="life",
        description="Conway's Game of Life in your terminal",
    )
    parser.add_argument(
        "--version", action="version", version=f"%(prog)s v{__version__}"
    )
    parser.add_argument(
        "-p",
        "--pattern",
        choices=[pattern.name for pattern in patterns.get_patterns()],
        default="Blinker",
        help="take a pattern for the Game of Life (default: %(default)s)",
    )
    parser.add_argument(
        "-a",
        "--all",
        action="store_true",
        help="show all available patterns in a sequence",
    )
    parser.add_argument(
        "-v",
        "--view",
        choices=views.__all__,
        default="CLIView",
        help="display the life grid in a specific view (default: %(default)s)",
    )
    parser.add_argument(
        "-g",
        "--gen",
        metavar="NUM_GENERATIONS",
        type=int,
        default=10,
        help="number of generations (default: %(default)s)",
    )
    parser.add_argument(
        "-f",
        "--fps",
        metavar="FRAMES_PER_SECOND",
        type=int,
        default=7,
        help="frames per second (default: %(default)s)",
    )
    return parser.parse_args()
