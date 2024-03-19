import pandas as pd

# This code takes the excel file and stores all the sheets as dataframes in a dictionary. 
# Each dataframe then has a key to fetch it. The key is the name of the sheet. 
# The dictionary is named "dfs" which is short for "dataframes".

# First I load the Excel file and register each sheet in a dictionary for easy access.

# Define the file path
file_path = 'C:\\Users\\Johan\\Desktop\\Python\\ledighed.xlsx'

# Create an ExcelFile object
excel_file = pd.ExcelFile(file_path)

# Get the sheet names
sheet_names = excel_file.sheet_names

sheet_names

# Create an empty dictionary to store DataFrames
dfs = {}

# Iterate over each sheet name and store sheet as a dataframe and store it in the dictionary.
for sheet_name in sheet_names:
    # Read the sheet into a DataFrame
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    # Store the DataFrame in the dictionary
    dfs[sheet_name] = df

# Now you have a dictionary 'dfs' containing DataFrames for each sheet
# You can access each DataFrame using the sheet name as the key
    
import pickle

# Define the file path where you want to save the dictionary
file_path2 = 'C:\\Users\\Johan\\Desktop\\Python\\dictionary.pkl'

# Save the dictionary to a file
with open(file_path2, 'wb') as f:
    pickle.dump(dfs, f)

# The file has now been created and stored on my PC on my desktop in a folder named "python".