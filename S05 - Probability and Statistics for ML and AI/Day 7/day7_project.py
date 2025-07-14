# # url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"

import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load Dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)

# # Inspect Data
# print(df.info())
# print(df.describe())

# del df["sex"]
# del df["smoker"]
# del df["day"]
# del df["time"]

# # Visualize Distributions
# # sns.histplot(df["total_bill"], kde=True)
# # plt.title("Distribution of Total Bill")
# # plt.show()

# # Correlation heatmap
# sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
# plt.title("Correlation Heatmap")
# plt.show()


# from scipy.stats import ttest_ind

# # Seperate data by gender
# male_tips = df[df['sex'] == 'Male']['tip']
# female_tips = df[df['sex'] == 'Female']['tip']

# # Perform t-test
# t_stat, p_value = ttest_ind(male_tips, female_tips)
# print("T-Statistic: ", t_stat)
# print("P-Value: ", p_value)

# # Interpret results
# alpha = 0.05
# if p_value <= alpha:
#     print("Reject all null hypothesis: Significant difference.")
# else:
#     print("Fail to Reject all null hypothesis: NO Significant difference.")

# Define variables
X = df['total_bill'].values.reshape(-1, 1)
y = df['tip'].values

# Fit linear regression
model = LinearRegression()
model.fit(X, y)

# Output coefficients
print("Slope: ", model.coef_[0])
print("Intercept: ", model.intercept_)
print("R-Squared:", model.score(X, y))

# Plot regression
sns.scatterplot(x=df['total_bill'], y=df['tip'], color="blue")
plt.plot(df['total_bill'], model.predict(X), color="red", label="Regression Line")
plt.title("Total Bill vs Tip")
plt.legend()
plt.show()











