import time
from pathlib import Path
from preprocess import preprocess_folder
from enhance_edges import run_stage4


def run_batch_pipeline():
    start_time = time.time()
    print("=== ArchaeoScript AI: Day 5 Batch Preprocessing Pipeline ===")

    raw_base = Path("data/raw")
    proc_base = Path("data/processed")
    stage4_base = Path("data/stage4")

    for script_name in ["indus", "brahmi"]:
        print(f"\n--- Processing [{script_name.upper()}] ---")
        preprocess_folder(raw_base / script_name, proc_base / script_name)
        run_stage4(proc_base / script_name, stage4_base / script_name)

    elapsed = time.time() - start_time
    print(f"\n=== Pipeline Completed in {elapsed:.2f}s ===")


if __name__ == "__main__":
    run_batch_pipeline()
    