"""
nlp_analysis.py
Text sentiment analysis and word cloud generation.
"""

import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from textblob import TextBlob


def ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)


def sentiment_analysis(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df['sentiment_polarity'] = df['clean_text'].apply(lambda x: TextBlob(x).sentiment.polarity if x else 0)
    df['sentiment'] = df['sentiment_polarity'].apply(
        lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Neutral"
    )
    return df


def plot_sentiment(df: pd.DataFrame, outdir="outputs/plots"):
    ensure_dir(outdir)
    plt.figure(figsize=(6,4))
    sns.countplot(x="sentiment", data=df)
    plt.title("Sentiment Distribution")
    plt.savefig(os.path.join(outdir, "sentiment_distribution.png"))
    plt.close()


def word_cloud(df: pd.DataFrame, outdir="outputs/plots"):
    ensure_dir(outdir)
    text = " ".join(df['clean_text'].tolist())
    wc = WordCloud(width=800, height=400, background_color="white").generate(text)

    plt.figure(figsize=(10,6))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.title("Word Cloud of Climate Discussions")
    plt.savefig(os.path.join(outdir, "wordcloud.png"))
    plt.close()
