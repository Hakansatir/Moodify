from __future__ import annotations
from pathlib import Path
import cv2


def read_image_bgr(path: Path):
    return cv2.imread(str(path))
