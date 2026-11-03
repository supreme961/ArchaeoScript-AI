"""Create the initial ArchaeoScript AI project structure."""

from pathlib import Path


DIRECTORIES = (
    "data",
    "src/preprocessing",
    "src/models",
    "src/utils",
    "backend",
    "frontend",
    "notebooks",
    "tests",
)


def create_project_structure(root: Path) -> None:
    """Create all required project directories below *root*."""
    for directory in DIRECTORIES:
        path = root / directory
        path.mkdir(parents=True, exist_ok=True)
        print(f"Created: {path.relative_to(root)}")


if __name__ == "__main__":
    create_project_structure(Path(__file__).resolve().parent)
    print("ArchaeoScript AI project structure is ready.")
