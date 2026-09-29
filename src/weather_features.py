"""Helpers for preparing weather variables used in the research design."""
import pandas as pd

WEATHER_COLUMNS = ["cloud", "rain", "temp", "sun"]

def prepare_weather(df: pd.DataFrame) -> pd.DataFrame:
    """Return a clean copy with numeric weather columns and missing rows removed."""
    out = df.copy()
    for col in WEATHER_COLUMNS:
        out[col] = pd.to_numeric(out[col], errors="coerce")
    return out.dropna(subset=WEATHER_COLUMNS)
