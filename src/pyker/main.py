"""Main entry module for the project."""

from pyker.cache import FileCache
from pyker.ipsum import ipsum_text
from pyker.lorem import lorem_text
from pyker.models import ComputationResult


def main() -> int:
    """Run the demo application."""
    result = ComputationResult(key="demo_result", value=f"{lorem_text()} {ipsum_text()}")

    cache = FileCache()
    cache.write_text(result.key, result.value)

    print(lorem_text())
    print(ipsum_text())
    print(f"cached: {result.key}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
