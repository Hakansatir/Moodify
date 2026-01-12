from pathlib import Path

ML_DIR = Path(__file__).resolve().parents[1]

# Dataset (PNG'ler burada - gitignore)
DATASET_DIR = ML_DIR / "data"

# Üretilen dosyalar
ARTIFACTS_DIR = ML_DIR / "artifacts"
DATA_FILE = ARTIFACTS_DIR / "data.txt"
LABELS_PATH = ARTIFACTS_DIR / "labels.json"

# Model çıktıları
MODELS_DIR = ML_DIR / "models"
MODEL_PATH = MODELS_DIR / "rf_model.pkl"

# Rapor çıktıları
REPORTS_DIR = ML_DIR / "reports"
METRICS_PATH = REPORTS_DIR / "metrics.txt"

# Prepare ayarları
EXPECTED_LANDMARK_LEN = 1404

# Train ayarları
RANDOM_STATE = 42
TEST_SIZE = 0.2