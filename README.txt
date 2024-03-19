IMPORTANT:
The script is designed for a specific dataset that is confidential.

Unemployment Data Analysis
Overview
This project aims to analyze unemployment data from multiple sources and consolidate it into a single dataset for easy analysis. The project involves cleaning and processing data from various Excel files, organizing it into a unified format, and performing analytical tasks on the aggregated dataset.

Features
Data Cleaning: The project includes routines to clean raw data extracted from Excel files, removing unnecessary rows and columns, and ensuring consistency across different datasets.
Data Aggregation: It aggregates cleaned data from multiple Excel files into a single Pandas DataFrame, facilitating easy analysis and visualization.
Profession Standardization: Similar professions with different names are standardized under common labels for better comparison and analysis.
Unemployment Rate Extraction: The project extracts unemployment rates for each standardized profession from the cleaned datasets and organizes them into the aggregated DataFrame.
Data Export: The aggregated dataset can be exported to a CSV file for further analysis using other tools or platforms.
Usage

Data Preparation:
- Place all raw data Excel files in a directory named data.
- Ensure Python 3.x and required libraries are installed (Pandas, NumPy).

Run the Script:
- Execute the Python script 'dfs creation.py'.
- Execute the Python script 'unemployment_data_analysis.py'.

The aggregated dataset will be stored in a CSV file named bp_ledighed_data.csv
Use this CSV file for further analysis using Python, Excel, or other data analysis tools.

Requirements
- Python 3.x
- Pandas

Contributors
Johannes Toft Bendtsen - johannestoftbendtsen@gmail.com