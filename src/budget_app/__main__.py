"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Budget App."""


if __name__ == "__main__":
    main(prog_name="budget-app")  # pragma: no cover
