# revenue_data_analysis

## Overview
The project analyzes a retail sales dataset to uncover insights about sales performance, customer behavior, and regional trends. Key features include
- Data Cleaning: Handling missing values, duplicates, and data type conversions.
- Exploratory Data Analysis (EDA): Summary statistics, sales breakdowns by category and region, and correlation analysis.
- Customer Segmentation: K-means clustering to group customers based on purchase behavior (total spend and quantity).
- Time-Series Analysis: Monthly sales trends with rolling averages for smoother insights.
- Visualizations: Static plots (matplotlib, seaborn) and interactive visualizations (Plotly) for enhanced interpretability.

## Workflow
1. Data Cleaning (data_cleaning.py):
- Converts dates to datetime format.
- Imputes missing prices with the mean price.
- Removes duplicates and calculates revenue (price × quantity).
- Saves cleaned data to data/cleaned_sales_data.csv.
2. Analysis (analysis.py):
- Computes summary statistics and sales breakdowns by category and region.
- Performs K-means clustering to segment customers based on normalized total revenue and quantity purchased.
- Saves segmentation results to data/customer_segments.csv.
3. Visualizations (visualization.py):
- Generates an interactive Plotly line plot of monthly sales with rolling averages (monthly_sales.html).
- Creates a static bar plot of total sales by category (category_sales.png).
- Produces a static scatter plot of customer segments (customer_segments.png).
4. Exploratory Analysis (exploratory_analysis.ipynb):
- Provides an interactive environment for exploring data distributions, correlations, and regional sales patterns.
