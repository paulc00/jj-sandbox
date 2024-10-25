"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Jujutsu Sandbox."""


# This is extremely cool and getting excessively so!
if __name__ == "__main__":
    main(prog_name="jj-sandbox")  # pragma: no cover
