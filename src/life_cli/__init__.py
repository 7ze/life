import argparse
import sys

from life_cli import cli, patterns, views


def main() -> int:
    args = cli.get_command_line_args()
    view_class: views.CLIView = getattr(views, args.view)
    if args.all:
        for pattern in patterns.get_patterns():
            _show_pattern(view_class, pattern, args)
    else:
        _show_pattern(view_class, patterns.get_pattern(name=args.pattern), args)
    return 0


def _show_pattern(
    view: views.CLIView,
    pattern: patterns.Pattern,
    args: argparse.Namespace,
) -> None:
    try:
        view(
            pattern=pattern,
            gen=args.gen,
            frame_rate=args.fps,
        ).draw()  # type: ignore
    except Exception as err:
        print(err, file=sys.stderr)
