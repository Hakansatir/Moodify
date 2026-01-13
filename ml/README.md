# 🧠 Moodify – Machine Learning Module

This module is responsible for **facial emotion recognition** using
computer vision and classical machine learning techniques.

It covers the **entire ML lifecycle**:
- Dataset preparation
- Feature extraction (face landmarks)
- Model training
- Evaluation & reporting
- Live inference via webcam

The module follows **Clean Architecture principles** to ensure
maintainability, testability, and easy integration with backend services.

---

## 📁 Project Structure

```text
ml/
├─ data/                 # Raw image dataset (ignored by git)
│  ├─ angry/
│  ├─ happy/
│  ├─ neutral/
│  ├─ sad/
│  └─ surprised/
│
├─ artifacts/            # Generated artifacts
│  ├─ data.txt           # Extracted features (ignored)
│  └─ labels.json        # Label → index mapping
│
├─ models/               # Trained models (ignored)
│  └─ rf_model.pkl
│
├─ reports/              # Evaluation reports
│  └─ metrics.txt
│
├─ src/
│  ├─ infrastructure/    # External dependencies & IO
│  │  ├─ mediapipe_landmarks.py
│  │  ├─ image_io.py
│  │  ├─ dataset_io.py
│  │  ├─ model_loader.py
│  │  └─ labels.py
│  │
│  ├─ use_cases/         # Application logic
│  │  ├─ prepare_dataset.py
│  │  ├─ train.py
│  │  └─ live_inference.py
│  │
│  ├─ config.py          # Paths & hyperparameters
│  └─ __init__.py
│
├─ requirements.txt
└─ README.md
