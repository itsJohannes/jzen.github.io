import pandas as pd

# EXPLANATION OF FILE:
# This code takes the dictionary created by "Dfs creation.py" and manipulates its contents into a single big dataframe apptly named big_dataframe.

# Define the file path
file_path = 'C:\\Users\\Johan\\Desktop\\Python\\ledighed.xlsx'

# Create an ExcelFile object
excel_file = pd.ExcelFile(file_path)

# Get the sheet names
sheet_names = excel_file.sheet_names

#print(len(sheet_names))

import pickle

# Creating the dictionary each time you run the code takes too long. Therefore, I've saved the dictionary in a file on my PC with the Pickle package.
# I've done this in another python script named "Dfs creation.py".
# I now load that dictionary file.

# Define the file path from where you want to load the dictionary
file_path2 = 'C:\\Users\\Johan\\Desktop\\Python\\dictionary.pkl'

# Load the dictionary from the file
with open(file_path2, 'rb') as f:
    dfs = pickle.load(f)


# Check how it looks
#print(dfs['95_aug'])



# First I clean the dataframes a little.

# Create an empty dictionary to store modified dataframes
cleaned_dfs = {}

# Iterate over each dataframe in the original dictionary
for sheet_name, df in dfs.items():
    # Remove rows 1-7 and rows after row 55
    cleaned_df = df.iloc[5:57]
    
    # Ensure only the first 8 columns are retained
    cleaned_df = cleaned_df.iloc[:, :8]
    
    # Store the modified dataframe in the new dictionary
    cleaned_dfs[sheet_name] = cleaned_df


# Verify the result by printing  multiple dataframes in the new cleaned dictionary from different sheets/years.
# This allows me to make sure the cleaning process works fine for the different formats of the excel sheets.
print(cleaned_dfs['12_dec'])
print(cleaned_dfs['95_aug'])
print(cleaned_dfs['96_sep'])
print(cleaned_dfs['01_jan'])
print(cleaned_dfs['17_jun'])
# I also use this so I can see what I'm working with.
# This helped me at a point where I found out that the column index for the total unemployment across age groups was different for different dataframes in the dictionary.
# It has also made me realize there are some problems with the dataframes in the dictionary. Some of them have more columns that others, and I don't know why. 
# A potential fix is to make an if-statement that detects length of each dataframe and shortens it to be maximum of 8 columns. That should solve the issue.
    # Update, that only half solved the issue. I solved the other half writing a selection program which would fetch the correct column containg "I alt" or "Tilsammen". See line 197 ca.


# Now the real project begins. I need to manipulate the dataframes in the dictionary into a single dataframe containing a column for the date and columns for the different professions.

# I think a good first step is to create a string containing all of the professions in the datasets.
# Some of professions change names over time. I might be able to identify them if the change is to a similar name with this list.

# Initialize an empty set to store unique profession names
unique_professions = set()

# Iterate over each dataframe in the dictionary
for df in cleaned_dfs.values():
    # Extract the profession names from the first column (index 0). They are always positioned in the first column.
    professions = df.iloc[:, 0].dropna().unique()
    
    # Add the unique profession names to the set
    unique_professions.update(professions)

# Convert the set to a sorted list of unique profession names
unique_professions = sorted(unique_professions)

# Print the list containing all unique profession names
print(unique_professions)

# The list we get is the following:
#['1) For december 2012 er der sket en justering af uddannelsesgrupperne i MA', '1) Fra december 2012 er der sket en justering af uddannelsesgrupperne i MA', 'Agronom', 'Akad.ing.', 'Andre', 'Arkitekt', 'Arkitekt og Designer', 'Arkitekt og designer', 'Bac. Hum.', 'Bac. Nat.', 'Bac. Samf.', 'Bac.Hum.', 'Bac.Hum.1', 'Bac.Nat.', 'Bac.Nat.1', 'Bac.Samf.', 'Bibliotekar', 'Cand. IT', 'Cand. IT.', 'Cand. Merc.', 'Cand.Merc.', 'Cand.Scient.Tech.', 'Cand.scient.tek.', 'Civ. Ing.', 'Civ. ing.', 'Civ.ing.', "DJØF'ere", "DJØF'ere i alt", 'DJØF-området', 'Diplom Ing.', 'Diplom ing.', 'Dyrlæge', 'Erh.Sprog', 'Farmaceut', 'Forstkand.', 'HA', 'HD', 'Hortonom', 'Ingeniører i alt', 'Jordbrugsakad.', 'Jurist', 'Komm. og Sprog', 'København', 'Landinspek.', 'Landsk. Arkt.', 'Landsk.Arkt.', 'Ledighedsprocenten er ikke angivet, når antallet af observationer er mindre end 10', 'Levn.m.i&c', 'Levn.m.kand.', 'Læge', 'MA. Hum.', 'MA. Hum.1', 'MA. Nat.', 'MA. Nat.1', 'MA. Ph.d.', 'MA. Ph.d.1', 'MA. Samf.', 'MA. Samf.1', 'Mag.Bio/Geo', 'Mag.Hum.', 'Mag.Mat/Fys', 'Mag.Samf.', 'Magistre i alt', 'Mejeriing.', 'Musikudd.', 'Psykolog', 'Samf. Adm.', 'Samf.Adm.', 'Se sidste del af statistikken for en oversigt over uddannelsesgrupperingernes indhold', 'Tabel 4.2 Antal ledige i procent af antal forsikrede medlemmer - aldersfordelt', 'Tabel 4.4 Gns. antal ledige i procent af antal forsikrede medlemmer', 'Tandlæge', 'Tek.ing.', 'Teolog', 'Total', 'aldersfordelt', 'Økonom', 'Øvrige Mag.', 'Øvrige Mag.1']
# We have a few elements (like the first element) that are not important for this analysis. I will write a script to remove these now.

# Define a list of keywords that indicate non-profession entries
bad_keywords = [
    'Tabel',
    'antal',
    'fordelt',
    'observationer',
    'indhold',
    'gns.',
    'ikke angivet',
    '1)',
    'københavn'
]

# Initialize lists to store excluded and filtered professions
excluded_professions = []
filtered_professions = []
# To make sure we don't exclude anything important we also note down what we exclude in a list.

# Iterate through each profession
for prof in unique_professions:
    # Check if any bad keyword is present in the lowercase version of the profession string
    if any(keyword in prof.lower() for keyword in bad_keywords):
        # If a bad keyword is found, add the profession to the excluded list
        excluded_professions.append(prof)
    else:
        # If no bad keywords are found, add the profession to the filtered list
        filtered_professions.append(prof)

# Print the list of excluded professions
#print("Excluded professions:", excluded_professions)

# Print the list of filtered professions
#print("Filtered professions:", filtered_professions)

# As a safeguard we also create a list of the excluded entries so we can confirm we haven't excluded anything important.
# Having printed both excluded and filtered professions we can confirm we have only excluded the non-profession entries.


# Within the list containing the filtered professions there are many similar entries. As an example, the first of such occurances is "Arkitekt", "Arkitekt og Designer" and "Arkitekt og designer".
# Python, like many other languages, is case-sensitive
# We therefore want to combine these into a single variable so it is consistent over time. I have done this manually through MS Word and added it in a list below. (see "filtered professions.docx")

# List of filtered professions
filtered_professions_common_names = ['Agronom', 'Akad.ing.', 'Andre', 'Arkitekt', 'Bac. Hum.', 'Bac. Nat.', 'Bac. Samf.', 'Bibliotekar', 'Cand. IT.', 'Cand. Merc.', 'Cand.scient.tek.', 'Civ. ing.', "DJØF'ere i alt", 'Diplom ing.', 'Dyrlæge', 'Farmaceut', 'Forstkand.', 'HA', 'HD', 'Hortonom', 'Ingeniører i alt', 'Jordbrugsakad.', 'Jurist', 'Komm. og Sprog', 'Landinspek.', 'Landsk. Arkt.', 'Levn.m.kand.', 'Læge', 'MA. Hum.', 'MA. Nat.', 'MA. Ph.d.', 'MA. Samf.', 'Magistre i alt', 'Mejeriing.', 'Musikudd.', 'Psykolog', 'Samf. Adm.', 'Tandlæge', 'Tek.ing.', 'Teolog', 'Total', 'Økonom', 'Øvrige Mag.']

# Create an empty dataframe to store the final data. The columns will be the filtered professions
big_dataframe = pd.DataFrame(columns=['Date'] + filtered_professions_common_names)

# Print the empty dataframe
print(big_dataframe)

# This dataframe will be the final dataframe. 



########## FAILED ATTEMPT BELOw ####### SKIP

# List of consistently named professions
# consistently_named_professions = ['Agronom', 'Akad.ing.', 'Andre', 'Bibliotekar', 'Dyrlæge', 'Erh.Sprog', 'Farmaceut', 'Forstkand.', 'HA', 'HD', 'Hortonom', 'Ingeniører i alt', 'Jordbrugsakad.', 'Jurist', 'Komm. og Sprog', 'Landinspek.', 'Læge', 'Magistre i alt', 'Mejeriing.', 'Musikudd.', 'Psykolog', 'Tandlæge', 'Tek.ing.', 'Teolog', 'Total', 'Økonom']

# List of similar professions grouped together
# similar_professions_grouped_together = [
#     ['Arkitekt', 'Arkitekt og Designer', 'Arkitekt og designer'],  # Group 1
#     ['Bac. Hum.', 'Bac.Hum.', 'Bac.Hum.1'],  # Group 2
#     ['Bac. Nat.', 'Bac.Nat.', 'Bac.Nat.1'],  # Group 3
#     ['Bac. Samf.', 'Bac.Samf.'],  # Group 4
#     ['Cand. IT', 'Cand. IT.'],  # Group 5
#     ['Cand. Merc.', 'Cand.Merc.'],  # Group 6
#     ['Cand.Scient.Tech.', 'Cand.scient.tek.'],  # Group 7
#     ['Civ. Ing.', 'Civ. ing.', 'Civ.ing.'],  # Group 8
#     ["DJØF'ere", "DJØF'ere i alt", 'DJØF-området'],  # Group 9
#     ['SimilarProfession4', 'SimilarProfession5', 'SimilarProfession6', ...],  # Group 10
#     ['SimilarProfession4', 'SimilarProfession5', 'SimilarProfession6', ...],  # Group 11
#     ['SimilarProfession4', 'SimilarProfession5', 'SimilarProfession6', ...],  # Group 12
#     ['SimilarProfession4', 'SimilarProfession5', 'SimilarProfession6', ...],  # Group 13
#     ['SimilarProfession4', 'SimilarProfession5', 'SimilarProfession6', ...],  # Group 14
#     ['SimilarProfession4', 'SimilarProfession5', 'SimilarProfession6', ...],  # Group 15
#     ['SimilarProfession4', 'SimilarProfession5', 'SimilarProfession6', ...],  # Group 16
#     ['SimilarProfession4', 'SimilarProfession5', 'SimilarProfession6', ...],  # Group 17
#     ['SimilarProfession4', 'SimilarProfession5', 'SimilarProfession6', ...],  # Group 18
# ]
#  ############ THE ABOVE CODE WAS AN ATTEMPT OF MAKING THE BELOW CODE SIMPLER ANd SHORTER TO AVOID A LOT OF MANUAL CODING ########## 




# I now need to run a loop that iterates over each dataframe in the dictionary, extracts the relevant data, and inserts it into the empty dataframe.

# Initialize the current row index
current_row_index = 0

# Iterate over each dataframe in the cleaned dictionary
for sheet_name, df in cleaned_dfs.items():
    # Initialize the last column index as None
    column_index = None
    
    # Iterate over the first 5 rows of the dataframe to find the "I alt" or "Tilsammen" column. This can be modified to look for age groups instead.
    for index, row in df.head(5).iterrows():
        # Check if the row contains "I alt" or "Tilsammen"
        if "I alt" in row.values or "Tilsammen" in row.values:
            # Get the index of the column containing "I alt" or "Tilsammen"
            column_index = row.index[(row == "I alt") | (row == "Tilsammen")][0] # Stores the name of the column
            column_index = df.columns.get_loc(column_index) # Fetches the number index of the column given the name
            #print(last_column_index) # Used this to make sure no mistakes were happening
            break  # Exit the loop once found
    
    # Check if the last_column_index is found
    if column_index is not None:

        # If found, iterate over each row in the dataframe
        for _, row in df.iterrows():
            # Extract the profession from column 0. The professions are always in column 0.
            profession = row.iloc[0]

            # Check if the profession matches any of the filtered professions
            if profession in filtered_professions:
                # Extract the unemployment data from the last column
                unemployment_data = row.iloc[column_index]
                
                # Find the common name for the profession
                if profession in ['Arkitekt og designer', 'Arkitekt og Designer', 'Arkitekt']:
                    common_profession = 'Arkitekt'
                elif profession in ['Bac. Hum.', 'Bac.Hum.', 'Bac.Hum.1']:
                    common_profession = 'Bac. Hum.'
                elif profession in ['Bac. Nat.', 'Bac.Nat.', 'Bac.Nat.1']:
                    common_profession = 'Bac. Nat.'
                elif profession in ['Bac. Samf.', 'Bac.Samf.']:
                    common_profession = 'Bac. Samf.'
                elif profession in ['Cand. IT', 'Cand. IT.']:
                    common_profession = 'Cand. IT.'
                elif profession in ['Cand. Merc.', 'Cand.Merc.']:
                    common_profession = 'Cand. Merc.'
                elif profession in ['Cand.Scient.Tech.', 'Cand.scient.tek.']:
                    common_profession = 'Cand.scient.tek.'
                elif profession in ['Civ. Ing.', 'Civ. ing.', 'Civ.ing.']:
                    common_profession = 'Civ. ing.'
                elif profession in ["DJØF'ere", "DJØF'ere i alt", 'DJØF-området']:
                    common_profession = "DJØF'ere i alt"
                elif profession in ['Diplom Ing.', 'Diplom ing.']:
                    common_profession = 'Diplom ing.'
                elif profession in ['Landsk. Arkt.', 'Landsk.Arkt.']:
                    common_profession = 'Landsk. Arkt.'
                elif profession in ['Levn.m.i&c', 'Levn.m.kand.' ]:
                    common_profession = 'Levn.m.kand.'
                elif profession in ['MA. Hum.', 'MA. Hum.1', 'Mag.Hum.']:
                    common_profession = 'MA. Hum.'
                elif profession in ['MA. Nat.', 'MA. Nat.1', 'Mag.Bio/Geo']:
                    common_profession = 'MA. Nat.'
                elif profession in ['MA. Ph.d.', 'MA. Ph.d.1', 'Mag.Mat/Fys']:
                    common_profession = 'MA. Ph.d.'
                elif profession in ['MA. Samf.', 'MA. Samf.1', 'Mag.Samf.']:
                    common_profession = 'MA. Samf.'
                elif profession in ['Samf. Adm.', 'Samf.Adm.']:
                    common_profession = 'Samf. Adm.'
                elif profession in ['Øvrige Mag.', 'Øvrige Mag.1']:
                    common_profession = 'Øvrige Mag.'
                elif profession in ['Agronom']:
                    common_profession = 'Agronom'
                elif profession in ['Akad.ing.']:
                    common_profession = 'Akad.ing.'
                elif profession in ['Andre']:
                    common_profession = 'Andre'
                elif profession in ['Bibliotekar']:
                    common_profession = 'Bibliotekar'
                elif profession in ['Dyrlæge']:
                    common_profession = 'Dyrlæge'
                elif profession in ['Farmaceut']:
                    common_profession = 'Farmaceut'
                elif profession in ['Forstkand.']:
                    common_profession = 'Forstkand.'
                elif profession in ['HA']:
                    common_profession = 'HA'
                elif profession in ['HD']:
                    common_profession = 'HD'
                elif profession in ['Hortonom']:
                    common_profession = 'Hortonom'
                elif profession in ['Ingeniører i alt']:
                    common_profession = 'Ingeniører i alt'
                elif profession in ['Jordbrugsakad.']:
                    common_profession = 'Jordbrugsakad.'
                elif profession in ['Jurist']:
                    common_profession = 'Jurist'
                elif profession in ['Komm. og Sprog', 'Erh.Sprog']:
                    common_profession = 'Komm. og Sprog'
                elif profession in ['Landinspek.']:
                    common_profession = 'Landinspek.'
                elif profession in ['Læge']:
                    common_profession = 'Læge'
                elif profession in ['Magistre i alt']:
                    common_profession = 'Magistre i alt'
                elif profession in ['Mejeriing.']:
                    common_profession = 'Mejeriing.'
                elif profession in ['Musikudd.']:
                    common_profession = 'Musikudd.'
                elif profession in ['Psykolog']:
                    common_profession = 'Psykolog'
                elif profession in ['Tandlæge']:
                    common_profession = 'Tandlæge'
                elif profession in ['Tek.ing.']:
                    common_profession = 'Tek.ing.'
                elif profession in ['Teolog']:
                    common_profession = 'Teolog'
                elif profession in ['Total']:
                    common_profession = 'Total'
                elif profession in ['Økonom']:
                    common_profession = 'Økonom'

                # Insert the unemployment data into the relevant column in the empty dataframe
                big_dataframe.loc[current_row_index, common_profession] = unemployment_data
                
        # Insert the dictionary key into the date column in the empty dataframe
        big_dataframe.loc[current_row_index, 'Date'] = sheet_name

        # Move to the next row index for the next dataframe
        current_row_index += 1

# Print the updated dataframe
print(big_dataframe)


# Export big_dataframe to a CSV file
big_dataframe.to_csv('bp_ledighed_data_total.csv', index=False)

print("big_dataframe exported to 'bp_ledighed_data.csv'")









