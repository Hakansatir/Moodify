from __future__ import annotations

from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np

from ml.src.config import DATASET_DIR, DATA_FILE, EXPECTED_LANDMARK_LEN, LABELS_PATH
from ml.src.infrastructure.dataset_io import save_json, save_txt_matrix
from ml.src.infrastructure.image_io import read_image_bgr
from ml.src.infrastructure.mediapipe_landmarks import extract_face_landmarks


def build_label_map(dataset_dir: Path) -> Dict[str, int]:
    emotions = sorted([p.name for p in dataset_dir.iterdir() if p.is_dir()])
    return {name: idx for idx, name in enumerate(emotions)}


def iter_images(dataset_dir: Path) -> List[Tuple[str, Path]]:
    items: List[Tuple[str, Path]] = []
    for emotion_dir in sorted([p for p in dataset_dir.iterdir() if p.is_dir()], key=lambda p: p.name):
        emotion = emotion_dir.name
        for img_path in sorted(emotion_dir.iterdir()):
            if img_path.is_file():
                items.append((emotion, img_path))
    return items


def run_prepare_dataset() -> Dict[str, str]:
    if not DATASET_DIR.exists():
        raise FileNotFoundError(f"Dataset directory not found: {DATASET_DIR}")

    label_map = build_label_map(DATASET_DIR)
    save_json(LABELS_PATH, label_map)

    output: List[List[float]] = []
    skipped = 0

    for emotion, img_path in iter_images(DATASET_DIR):
        image = read_image_bgr(img_path)
        if image is None:
            skipped += 1
            continue

        landmarks = extract_face_landmarks(image, draw=False, static_image_mode=True)

        if len(landmarks) == EXPECTED_LANDMARK_LEN:
            row = landmarks + [float(label_map[emotion])]
            output.append(row)
        else:
            skipped += 1

    arr = np.asarray(output, dtype=np.float32)
    save_txt_matrix(DATA_FILE, arr)

    return {
        "data_file": str(DATA_FILE),
        "labels_file": str(LABELS_PATH),
        "num_rows": str(arr.shape[0]),
        "skipped": str(skipped),
    }


if __name__ == "__main__":
    result = run_prepare_dataset()
    print("Dataset prepared ✅")
    print(result)
