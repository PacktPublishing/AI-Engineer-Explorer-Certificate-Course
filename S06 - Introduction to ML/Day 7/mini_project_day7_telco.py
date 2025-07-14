# Task 1: Perform EDA and Preprocessing
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Load Telco Customer Churn Dataset
df_telco = pd.read_csv('Telco-Customer-Churn.csv')

# Encode categorical variables
le = LabelEncoder()
df_telco['churn'] = le.fit_transform(df_telco['churn'])
df_telco['gender'] = le.fit_transform(df_telco['gender'])
df_telco['contract_type'] = le.fit_transform(df_telco['contract_type'])
df_telco['payment_method'] = le.fit_transform(df_telco['payment_method'])

# Define features and target
X = df_telco.drop(columns=['churn'])
y = df_telco['churn']

# Scale Features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train logistic regression model
log_model = LogisticRegression(max_iter=200)
log_model.fit(X_train, y_train)

# Train k-NN model
knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X_train, y_train)

#Evaluate models
log_pred = log_model.predict(X_test)
knn_pred = knn_model.predict(X_test)

print("\n Logistic Regression Clasification report:")
print(classification_report(y_test, log_pred))

print("\n k-NN  Clasification report:")
print(classification_report(y_test, knn_pred))

#Confusion Matric for Logistic Regression
print("Confusion Matrix: \n", confusion_matrix(y_test, log_pred))

# # Inspect Data
# print(df_telco.info())
# print(df_telco.describe())

# # Visualize churn distribution
# sns.countplot(x='churn', data=df_telco)
# plt.title("Churn Distribution")
# plt.show()

# # Handle missing values
# df_telco.fillna(df_telco.mean(), inplace=True)