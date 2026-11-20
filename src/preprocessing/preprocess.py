from pathlib import Path
import cv2


def apply_clahe_gray(img_bgr):
    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    return clahe.apply(gray)


def preprocess_folder(input_dir: Path, output_dir: Path):
    if not input_dir.exists():
        print(f"[SKIP] Input folder not found: {input_dir}")
        return

    output_dir.mkdir(parents=True, exist_ok=True)
    exts = {".jpg", ".jpeg", ".png", ".webp", ".bmp"}
    image_files = [p for p in input_dir.rglob("*") if p.is_file() and p.suffix.lower() in exts]

    processed_count = 0
    failed_count = 0

    for img_path in image_files:
        img = cv2.imread(str(img_path))
        if img is None:
            failed_count += 1
            continue

        enhanced = apply_clahe_gray(img)
        rel_path = img_path.relative_to(input_dir).with_suffix(".png")
        out_path = output_dir / rel_path
        out_path.parent.mkdir(parents=True, exist_ok=True)

        if cv2.imwrite(str(out_path), enhanced):
            processed_count += 1
        else:
            failed_count += 1

    print(f"{input_dir} -> {output_dir} | Processed: {processed_count} | Failed: {failed_count}")


if __name__ == "__main__":
    raw_base = Path("data/raw")
    proc_base = Path("data/processed")

    preprocess_folder(raw_base / "indus", proc_base / "indus")
    preprocess_folder(raw_base / "brahmi", proc_base / "brahmi")