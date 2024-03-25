IMPORTANT:
The script is designed for a specific dataset that is confidential.

Unemployment Data Analysis
Overview
This project was created for an exam project at Copenhagen Business School.
This project aims to analyze unemployment data from multiple sheets within an Excel file and consolidate it into a single dataset for easy analysis. The project involves cleaning and processing data from multiple Excel sheets, organizing it into a unified format, and performing analytical tasks on the aggregated dataset.

Features
Data Cleaning: The project includes routines to clean raw data extracted from Excel sheets, removing unnecessary rows and columns, and ensuring consistency across different datasets.
Data Aggregation: It aggregates cleaned data from multiple Excel sheets into a single Pandas DataFrame, facilitating easy analysis and visualization.
Profession Standardization: Similar professions with different names are standardized under common labels for better comparison and analysis.
Unemployment Rate Extraction: The project extracts unemployment rates for each standardized profession from the cleaned datasets and organizes them into the aggregated DataFrame.
Data Export: The aggregated dataset can be exported to a CSV file for further analysis using other tools or platforms.

Run the Script:
- Ensure Python 3.x and required libraries are installed (Pandas, NumPy).
- Execute the Python script 'dfs creation.py'. This file creates a dictionary containing a dataframe of each excel sheet.
- Execute the Python script 'unemployment_data_analysis.py'. This file takes this dictionary and extracts the relevant data into a single dataframe for easy analysis.

The aggregated dataset will be stored in a CSV file named bp_ledighed_data.csv
Use this CSV file for further analysis using Python, Excel, R, or other data analysis tools.

Requirements
- Python 3.x
- Pandas
- Pickle

Contributors
Johannes Toft Bendtsen - johannestoftbendtsen@gmail.com
