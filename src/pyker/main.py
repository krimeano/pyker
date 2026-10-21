"""Main entry module for the project."""

from pyker.lorem import lorem_text
from pyker.ipsum import ipsum_text


def main() -> int:
    """Run the demo application."""
    print(lorem_text())
    print(ipsum_text())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
