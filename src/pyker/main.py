"""Main entry module for the project."""

from pyker.cache import FileCache
from pyker.models import ComputationResult


def main() -> int:
    """Run the demo application."""
    result = ComputationResult(key="demo_result", value="pyker demo")

    cache = FileCache()
    cache.write_text(result.key, result.value)

    print(result.value)
    print(f"cached: {result.key}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
