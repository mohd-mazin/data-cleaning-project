Data Cleaning Project – World Happiness Report 2026
📖 Overview
This project demonstrates data cleaning and exploratory analysis using Python and Pandas.
The dataset used is the World Happiness Report 2026 – Official Rankings, which contains happiness scores and contributing factors for 130 countries worldwide.

The project is structured into three scripts:

pandas_basics.py → Load and explore the dataset

data_cleaning.py → Clean and preprocess the dataset

data_analysis.py → Perform analysis and generate insights

📂 Project Structure
Code
data-cleaning-project/
│
├── pandas_basics.py       # Basic dataset exploration
├── data_cleaning.py       # Cleaning and preprocessing
├── data_analysis.py       # Analysis and insights
└── sample_dataset.csv     # World Happiness Report 2026 dataset
📊 Dataset
Source: World Happiness Report 2026 – Kaggle

Columns:

rank – Global ranking by happiness score

country – Country name

region – Geographic region

score – Happiness score (0–10 scale)

gdp_per_capita – Economic contribution

social_support – Community/family support

healthy_life_expectancy – Health factor

freedom – Freedom to make life choices

generosity – Willingness to help others

corruption – Perception of corruption

▶️ How to Run
Install dependencies

powershell
pip install pandas matplotlib seaborn
Run scripts in PowerShell

powershell
python pandas_basics.py
python data_cleaning.py
python data_analysis.py
Outputs

pandas_basics.py → Prints dataset overview

data_cleaning.py → Saves cleaned_dataset.csv

data_analysis.py → Displays insights and plots

🎯 Learning Goals
Practice data cleaning: handling missing values, duplicates, and formatting

Explore data analysis: grouping, sorting, correlations

Build confidence with Pandas workflows

Prepare for real-world Data Science projects
