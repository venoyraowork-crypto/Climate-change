"""
data_processing.py
Handles loading and cleaning of climate dataset.
"""

import pandas as pd
import re

def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Convert date column to datetime
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # Fill missing numeric values
    df['likesCount'] = pd.to_numeric(df['likesCount'], errors='coerce').fillna(0).astype(int)
    df['commentsCount'] = pd.to_numeric(df['commentsCount'], errors='coerce').fillna(0).astype(int)

    # Clean text column
    def clean_text(text):
        if pd.isna(text):
            return ""
        text = re.sub(r"http\S+", "", text)  # remove URLs
        text = re.sub(r"[^a-zA-Z\s]", "", text)  # keep only letters
        return text.lower().strip()

    df['clean_text'] = df['text'].apply(clean_text)

    return df


if __name__ == "__main__":
    df = load_data("climate_nasa.csv")
    df_clean = clean_data(df)
    print(df_clean.head())
