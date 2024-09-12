import pandas as pd

data = pd.read_csv('missing.csv')

# print(data.to_string())

# show the boolean dataframe             
# print(" \nshow the boolean Dataframe : \n\n", data.isnull()) 
# print("\nshow the boolean Dataframe :\n\n",data.isna().sum())

# Count total NaN at each column in a DataFrame 
print(" \nTotal Missing values at each column in a DataFrame : \n\n", data.isnull().sum())

# Prints only missing values rows
# print(data[data.isnull().any(axis=1)].to_string())