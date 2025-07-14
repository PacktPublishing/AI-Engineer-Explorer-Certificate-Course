# Task 1: Perform EDA and Preprocessing
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load Dataset
data = fetch_california_housing(as_frame=True)
df = data.frame

# Define features and target
X = df[['MedInc', 'HouseAge', 'AveRooms']]
y = df['MedHouseVal']

# Inspect data
# print(df.info())
# print(df.describe())

# # Visualize relationships
# sns.pairplot(df, vars=['MedInc', 'AveRooms', 'HouseAge', 'MedHouseVal'])
# plt.show()

# # Check for missing values
# print("Missing Values: \n", df.isnull().sum())

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make Predictions
y_pred = model.predict(X_test)

# Evaluate performance 
mse = mean_squared_error(y_test, y_pred)
print("Linear Regression MSE:", mse)
