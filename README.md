🎬📊 Movie Budget and IMDb Rating Analysis 🍿
Project Overview & Motivation

Movies have always been one of the biggest parts of the entertainment industry, and I have always been curious about why some movies become extremely successful while others do not. As someone who enjoys watching movies and checking IMDb ratings regularly, I wanted to explore whether financial investment actually affects audience reception and movie success.

In this project, I analyzed movie data between 1980 and 2020 to understand the relationship between movie budgets, IMDb ratings, popularity, and revenue. I was especially interested in seeing whether bigger budgets lead to higher IMDb ratings or if audience satisfaction depends on other factors as well.

The goal of the project was to combine data analysis, visualization, and basic machine learning techniques to better understand movie success using real world movie data.

Data Source: Where did i get the data, How i collect it🌐

The main dataset used in this project was obtained from Kaggle and included information about movies such as:

movie names
genres
release years
IMDb scores
vote counts
budgets
gross revenue
runtime

To improve the dataset, I also used IMDb official datasets:

title.basics.tsv
title.ratings.tsv

Using movie titles and release years, I matched the movies with IMDb data and added IMDb IDs, IMDb ratings, vote counts, and genres to the dataset.

The IMDb enrichment process achieved approximately a 97% successful match rate.

Data Analysis 🔍

After cleaning and preprocessing the dataset, I performed several different analyses to better understand movie success and popularity.

IMDb Enrichment

The dataset was enriched using IMDb official data. I created a visualization to compare matched and unmatched movies after the enrichment process.

Budget vs IMDb Rating

Using scatter plots, I analyzed the relationship between movie budgets and IMDb ratings.

The results showed that having a larger budget does not necessarily guarantee higher IMDb ratings. Many lower budget movies also received strong audience ratings.

Budget vs Gross Revenue

I also explored the relationship between budget and gross revenue.

Compared to IMDb ratings, budget appeared to have a stronger relationship with revenue. In general, higher budget movies tended to generate more revenue overall.

Hypothesis Testing

Movies were divided into high budget and low budget groups based on the median budget value.

A t-test was applied to compare IMDb ratings between these groups and evaluate whether the differences were statistically significant.

Machine Learning

A Linear Regression model was used to predict movie popularity using variables such as:

budget
IMDb score
runtime

The model performance was evaluated using:

R² Score
Mean Squared Error (MSE)

Although the model captured some general trends, the results showed that movie success cannot be fully explained by budget and ratings alone.

Visualizations 📈
Score Distribution

Budget vs Popularity

Actual vs Predicted Values

Conclusion

The project showed that movie budget alone is not enough to explain audience ratings and popularity.

While higher budget movies generally earned more revenue, IMDb ratings depended on many additional factors beyond financial investment.

Overall, the analysis demonstrated that movie success is influenced by a combination of budget, audience reception, and other external factors.
