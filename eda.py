"""
eda.py
Exploratory Data Analysis for climate dataset.
"""

import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)


def time_series(df: pd.DataFrame, outdir="outputs/plots"):
    ensure_dir(outdir)
    df['month'] = df['date'].dt.to_period("M")
    trend = df.groupby('month').size()

    plt.figure(figsize=(10,5))
    trend.plot(kind="line", marker="o")
    plt.title("Posts Over Time")
    plt.ylabel("Number of Posts")
    plt.xlabel("Month")
    plt.savefig(os.path.join(outdir, "posts_over_time.png"))
    plt.close()


def engagement_distribution(df: pd.DataFrame, outdir="outputs/plots"):
    ensure_dir(outdir)

    plt.figure(figsize=(6,4))
    sns.histplot(df['likesCount'], bins=30, kde=False)
    plt.title("Likes Distribution")
    plt.savefig(os.path.join(outdir, "likes_distribution.png"))
    plt.close()

    plt.figure(figsize=(6,4))
    sns.histplot(df['commentsCount'], bins=30, kde=False)
    plt.title("Comments Distribution")
    plt.savefig(os.path.join(outdir, "comments_distribution.png"))
    plt.close()


def top_users(df: pd.DataFrame, outdir="outputs/reports"):
    ensure_dir(outdir)
    top_users_df = df['profileName'].value_counts().head(10).reset_index()
    top_users_df.columns = ["profileName", "post_count"]
    top_users_df.to_csv(os.path.join(outdir, "top_users.csv"), index=False)
