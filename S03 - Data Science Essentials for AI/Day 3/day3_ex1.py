#https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv

import pandas as pd

# Load Dataset
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

# Explore structure
# print("First 5 rows: \n", df.head())
# print("Last 5 rows: \n", df.tail())
# print(df.describe())

selected_columns = df[["species", "sepal_length"]]
# print("Selected Columns: \n", selected_columns)

filtered_rows = df[(df["sepal_length"] > 5.0) & (df["species"] == "setosa")]
print("Filteres Rows: \n", filtered_rows)
