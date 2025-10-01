This project analyzes climate change–related discussions from the NASA dataset.
It applies data preprocessing, exploratory data analysis (EDA), and NLP (sentiment analysis, word cloud) to understand engagement trends, user activity, and discussion themes.

📁 Project Structure
climate-analysis/
│── data_processing.py      # Load & clean dataset
│── eda.py                  # Exploratory Data Analysis (time, engagement, users)
│── nlp_analysis.py         # Sentiment analysis & word cloud
│── reporting.py            # Generate summary reports
│── run.py                  # Main script to run the pipeline
│── requirements.txt        # Dependencies
│── climate_nasa.csv        # Dataset (sample)
│── outputs/
│   ├── plots/              # Generated visualizations
│   └── reports/            # CSV reports

▶️ Usage
Run the full pipeline with:
python run.py --data climate_nasa.csv --out outputs


This will:
Clean the dataset
Perform EDA (time trends, engagement, top users)
Run NLP (sentiment analysis, word cloud)
Export plots (outputs/plots/) and summary reports (outputs/reports/)

📊 Features

Data Cleaning
Convert dates to datetime
Handle missing likes/comments
Clean and normalize text

Exploratory Data Analysis
Posts over time
Likes & comments distribution
Top active uses

Natural Language Processing
Sentiment analysis (Positive / Neutral / Negative)
Word cloud visualization of key terms

Reports
Sentiment summary (CSV)
Top users (CSV)
Top liked posts (CSV)
Top users (CSV)

Top liked posts (CSV)
