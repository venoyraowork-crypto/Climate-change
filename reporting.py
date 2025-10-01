"""
reporting.py
Exports summaries for reporting.
"""

import os
import pandas as pd


def ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)


def export_reports(df: pd.DataFrame, outdir="outputs/reports"):
    ensure_dir(outdir)

    # Sentiment summary
    sentiment_summary = df['sentiment'].value_counts().reset_index()
    sentiment_summary.columns = ["sentiment", "count"]
    sentiment_summary.to_csv(os.path.join(outdir, "sentiment_summary.csv"), index=False)

    # Top liked posts
    top_likes = df[['date','likesCount','clean_text']].sort_values("likesCount", ascending=False).head(10)
    top_likes.to_csv(os.path.join(outdir, "top_liked_posts.csv"), index=False)
