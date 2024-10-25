"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Jujutsu Sandbox."""


if __name__ == "__main__":
    main(prog_name="jj-sandbox")  # pragma: no cover
