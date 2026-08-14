from pathlib import Path

# Project root directory
ROOT = Path(__file__).resolve().parent.parent

RAW_DATA = ROOT / "data" / "raw" / "ev_population_data.csv"

CLEANED_DATA = ROOT / "data" / "cleaned" / "ev_population_cleaned.csv"

FIGURES_DIR = ROOT / "reports" / "figures"

FIGURES_DIR.mkdir(parents=True, exist_ok=True)