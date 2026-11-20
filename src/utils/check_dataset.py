from pathlib import Path
from PIL import Image


def audit_folder(folder_path: Path):
    if not folder_path.exists():
        print(f"[MISSING] {folder_path}")
        return

    exts = {".jpg", ".jpeg", ".png", ".webp", ".bmp"}
    files = [p for p in folder_path.rglob("*") if p.is_file() and p.suffix.lower() in exts]
    valid_count = 0
    corrupt_files = []

    for img_path in files:
        try:
            with Image.open(img_path) as img:
                img.verify()
            valid_count += 1
        except Exception:
            corrupt_files.append(img_path.name)

    print(f"Folder: {folder_path} | Valid Images: {valid_count} | Corrupt: {len(corrupt_files)}")
    if corrupt_files:
        print("  Corrupt files:", corrupt_files)


if __name__ == "__main__":
    base_dir = Path("data/raw")
    audit_folder(base_dir / "indus")
    audit_folder(base_dir / "brahmi")