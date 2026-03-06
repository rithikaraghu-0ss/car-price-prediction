import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
from sklearn.metrics import r2_score
import pickle

# Load data
df = pd.read_csv('data/car_data.csv')

# Preprocessing
# We can see that 'Car_Name' is actually the model. 
# For simplicity, we will use Car_Name as our primary categorical feature along with others.
# The user theory mentions 'Car Company' and 'Model Name'. 
# In this dataset, Car_Name is the model name.

# Target: Selling_Price
# Features: Car_Name, Year, Kms_Driven, Fuel_Type, Seller_Type, Transmission

X = df.drop(columns=['Selling_Price', 'Present_Price', 'Owner'])
y = df['Selling_Price']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# OneHotEncoder for categorical features
ohe = OneHotEncoder()
ohe.fit(X[['Car_Name', 'Fuel_Type', 'Seller_Type', 'Transmission']])

column_trans = make_column_transformer(
    (OneHotEncoder(categories=ohe.categories_), ['Car_Name', 'Fuel_Type', 'Seller_Type', 'Transmission']),
    remainder='passthrough'
)

# Linear Regression Model
lr = LinearRegression()

# Pipeline
pipe = make_pipeline(column_trans, lr)

# Training
pipe.fit(X_train, y_train)

# Evaluation
y_pred = pipe.predict(X_test)
print(f"R2 Score: {r2_score(y_test, y_pred)}")

# Save the model
with open('model/car_price_model.pkl', 'wb') as f:
    pickle.dump(pipe, f)

print("Model saved to model/car_price_model.pkl")
