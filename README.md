DSA-210 Project – Movie Budget and IMDb Rating Analysis
Project Overview 🎬

This project analyzes the relationship between movie budgets, IMDb ratings, and movie popularity using movie data between 1980 and 2020.

The main goal of the project is to understand whether higher budget movies tend to receive better IMDb ratings and generate higher revenue. The project also explores how variables such as votes, runtime, and ratings relate to movie success.

Dataset 📂

The main dataset was obtained from Kaggle and includes information about movies such as:

Movie Title
Genre
Release Year
IMDb Score
Votes
Budget
Gross Revenue
Runtime

To improve the analysis, the dataset was enriched using IMDb official datasets:

title.basics.tsv
title.ratings.tsv

Movies were matched using title and release year information. IMDb enrichment added:

IMDb IDs
IMDb ratings
IMDb vote counts
IMDb genres

The enrichment process achieved approximately a 97% match rate.

Data Analysis 🔍

The project includes several stages of analysis:

Data cleaning and preprocessing
IMDb data enrichment
Exploratory Data Analysis (EDA)
Correlation analysis
Hypothesis testing
Basic machine learning modeling

Several visualizations were created to analyze the relationships between movie variables.

Hypothesis Testing 📊

The project tested whether higher budget movies tend to receive higher IMDb ratings and popularity.

Movies were divided into high budget and low budget groups, and a t-test was applied to compare their IMDb ratings.

Machine Learning 🤖

A Linear Regression model was used to predict movie popularity using variables such as:

budget
IMDb score
runtime

Model performance:

R² Score: ~0.36
MSE: 21143358032.67

The results show that movie popularity can be partially explained by these variables, although many other external factors also affect success.

Visualizations 📈
Score Distribution

Budget vs Popularity

Actual vs Predicted Values

Conclusion

The analysis showed that higher movie budgets do not always guarantee higher IMDb ratings. However, movies with larger budgets generally tend to generate more revenue.

The IMDb enrichment process improved the dataset significantly and allowed more detailed analysis using ratings and vote counts.

Overall, the project suggests that movie success depends on many different factors, not only budget alone.
