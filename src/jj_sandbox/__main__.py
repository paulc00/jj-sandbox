"""Command-line interface."""
import click


# This is a superb implementation of this program.
# Maybe the best ever!
# How many comments is too many?
@click.command()
@click.version_option()
def main() -> None:
    """Jujutsu Sandbox."""


if __name__ == "__main__":
    main(prog_name="jj-sandbox")  # pragma: no cover
