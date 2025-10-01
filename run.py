"""
run.py
Main script to execute climate dataset analysis pipeline.
"""

import argparse
from data_processing import load_data, clean_data
import eda
import nlp_analysis
import reporting


def main(data_path, outdir="outputs"):
    # Load & clean
    df = load_data(data_path)
    df = clean_data(df)

    # EDA
    eda.time_series(df, outdir + "/plots")
    eda.engagement_distribution(df, outdir + "/plots")
    eda.top_users(df, outdir + "/reports")

    # NLP
    df = nlp_analysis.sentiment_analysis(df)
    nlp_analysis.plot_sentiment(df, outdir + "/plots")
    nlp_analysis.word_cloud(df, outdir + "/plots")

    # Reporting
    reporting.export_reports(df, outdir + "/reports")

    print("✅ Analysis complete. Check the outputs folder.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=str, default="climate_nasa.csv", help="Path to dataset")
    parser.add_argument("--out", type=str, default="outputs", help="Output directory")
    args = parser.parse_args()

    main(args.data, args.out)
