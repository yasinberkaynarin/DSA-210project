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

