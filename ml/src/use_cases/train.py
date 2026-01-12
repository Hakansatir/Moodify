from __future__ import annotations

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split

from ml.src.config import (
    DATA_FILE,
    METRICS_PATH,
    MODEL_PATH,
    RANDOM_STATE,
    TEST_SIZE,
)
from ml.src.infrastructure.storage import save_pickle, write_text


def run_training() -> dict:
    # 1) Load
    data = np.loadtxt(DATA_FILE)

    x = data[:, :-1]
    y = data[:, -1]

    # 2) Split
    x_train, x_test, y_train, y_test = train_test_split(
        x,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
        shuffle=True,
        stratify=y,
    )

    # 3) Train
    model = RandomForestClassifier(random_state=RANDOM_STATE)
    model.fit(x_train, y_train)

    # 4) Eval
    y_pred = model.predict(x_test)
    acc = accuracy_score(y_test, y_pred)

    cm = confusion_matrix(y_test, y_pred)

    # classification_report sınıf bazlı metrikleri verir (senin istediğin şey)
    report = classification_report(y_test, y_pred, digits=4)

    # 5) Persist
    save_pickle(model, MODEL_PATH)

    metrics_text = (
        f"Accuracy: {acc * 100:.2f}%\n\n"
        f"Confusion Matrix:\n{cm}\n\n"
        f"Classification Report:\n{report}\n"
    )
    write_text(METRICS_PATH, metrics_text)

    return {
        "accuracy": float(acc),
        "model_path": str(MODEL_PATH),
        "metrics_path": str(METRICS_PATH),
    }


if __name__ == "__main__":
    result = run_training()
    print(f"Saved model to: {result['model_path']}")
    print(f"Saved metrics to: {result['metrics_path']}")
    print(f"Accuracy: {result['accuracy'] * 100:.2f}%")
