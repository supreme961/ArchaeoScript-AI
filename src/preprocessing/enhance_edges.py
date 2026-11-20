from pathlib import Path
import cv2


def process_image_stages(gray_img):
    # 1. Noise reduction while keeping edges sharp
    denoised = cv2.bilateralFilter(gray_img, d=7, sigmaColor=50, sigmaSpace=50)

    # 2. Adaptive binarization for uneven lighting on seals/inscriptions
    binary = cv2.adaptiveThreshold(
        denoised,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        blockSize=15,
        C=4,
    )

    # 3. Canny edge detection for symbol contours
    edges = cv2.Canny(denoised, threshold1=50, threshold2=150)

    return denoised, binary, edges


def run_stage4(input_root: Path, output_root: Path):
    if not input_root.exists():
        print(f"[SKIP] Processed input folder not found: {input_root}")
        return

    exts = {".jpg", ".jpeg", ".png", ".webp", ".bmp"}
    image_files = [p for p in input_root.rglob("*") if p.is_file() and p.suffix.lower() in exts]

    count = 0
    for img_path in image_files:
        gray = cv2.imread(str(img_path), cv2.IMREAD_GRAYSCALE)
        if gray is None:
            continue

        _, binary, edges = process_image_stages(gray)
        rel_path = img_path.relative_to(input_root)

        bin_out = output_root / "binary" / rel_path
        edge_out = output_root / "edges" / rel_path
        bin_out.parent.mkdir(parents=True, exist_ok=True)
        edge_out.parent.mkdir(parents=True, exist_ok=True)

        cv2.imwrite(str(bin_out), binary)
        cv2.imwrite(str(edge_out), edges)
        count += 1

    print(f"Stage 4 complete for {input_root} -> Generated binary & edges for {count} images.")


if __name__ == "__main__":
    proc_base = Path("data/processed")
    stage4_base = Path("data/stage4")

    run_stage4(proc_base / "indus", stage4_base / "indus")
    run_stage4(proc_base / "brahmi", stage4_base / "brahmi")