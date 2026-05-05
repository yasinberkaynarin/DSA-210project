# -*- coding: utf-8 -*-
"""
yasin berkay narin
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from scipy.stats import ttest_ind


df = pd.read_csv("movies.csv")

df = df[['name','genre','year','score','votes','budget','gross','runtime']]


numeric_cols = ['year','score','votes','budget','gross','runtime']

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

df = df.dropna()

print("Dataset Shape:", df.shape)
print(df.head())





plt.figure(figsize=(8,5))
sns.histplot(df['score'], bins=30, kde=True)
plt.title("Distribution of IMDb Scores")
plt.show()


plt.figure(figsize=(8,5))
sns.scatterplot(data=df, x='budget', y='votes', alpha=0.6)
plt.title("Budget vs Popularity")
plt.show()



median_budget = df['budget'].median()

high_budget = df[df['budget'] >= median_budget]['votes']
low_budget  = df[df['budget'] < median_budget]['votes']

t_stat, p_value = ttest_ind(high_budget, low_budget, equal_var=False)

print("\n===== Hypothesis Test Result =====")
print("T-Statistic:", t_stat)
print("P-Value:", p_value)

if p_value < 0.05:
    print("Reject H0: High-budget and low-budget movies differ significantly in popularity.")
else:
    print("Fail to Reject H0: No significant difference found.")

# MACHINE LEARNING

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
X = df[['budget','score','runtime']]
y = df['votes']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("\n===== Machine Learning Result =====")
print("MSE:", mse)
print("R2 Score:", r2)
plt.figure(figsize=(6,6))
plt.scatter(y_test, y_pred, alpha=0.6)
plt.xlabel("Actual Votes")
plt.ylabel("Predicted Votes")
plt.title("Actual vs Predicted Popularity")
plt.show()
