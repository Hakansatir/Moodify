from __future__ import annotations

import cv2

from ml.src.config import MODEL_PATH, LABELS_PATH
from ml.src.infrastructure.mediapipe_landmarks import extract_face_landmarks
from ml.src.infrastructure.model_loader import load_model
from ml.src.infrastructure.labels import load_labels


def run_live_inference(camera_index: int = 0):
    model = load_model(MODEL_PATH)
    labels = load_labels(LABELS_PATH)

    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        raise RuntimeError("Camera could not be opened")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        landmarks = extract_face_landmarks(
            frame,
            draw=False,
            static_image_mode=False,
        )

        if landmarks:
            pred = model.predict([landmarks])[0]
            label = labels[int(pred)]

            cv2.putText(
                frame,
                label,
                (10, frame.shape[0] - 20),
                cv2.FONT_HERSHEY_SIMPLEX,
                2,
                (0, 255, 0),
                4,
            )

        cv2.imshow("Moodify - Live Inference", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run_live_inference()
