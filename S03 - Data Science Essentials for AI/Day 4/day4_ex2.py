import pandas as pd
import numpy as np

df1 = pd.DataFrame({
    "ID": [1,2,3],
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
})

df2 = pd.DataFrame({
    "ID": [1,2,3],
    "Score": [85, 90, 88]
})

print("Dataset 1: \n", df1)
print("Dataset 2: \n", df2)

merged = pd.merge(df1, df2, how="inner", on="ID")
print("Merged Dataset: \n", merged)

merged["Score_Percentage"] = (merged["Score"] / 200) * 100
print("Transformed Dataset \n", merged)