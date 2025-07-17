import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

def perform_analysis(data_path):

    #load clean data
    df = pd.read_csv(data_path)

    #summary statistics
    print("Summary Statistics: ")
    print(df.describe())

    #sales by category and region
    print("\nSales by Category: ")
    print(df.grouby('category')['revenue'].sum())
    print("\nSales by Region: ")
    print(df.groupby('region')['revenue'].sum())

    #customer segmentation
    customer_data = df.groupby('customer_id').agg({
        'revenue': 'sum',
        'quantity': 'sum'
    }).reset_index()

    #normalize data for clustering
    customer_data['revenue_norm'] = (customer_data['revenue'] - customer_data['revenue'].mean()) / customer_data['revenue'].std()
    customer_data['quantity_norm'] = (customer_data['quantity'] - customer_data['quantity'].mean()) / customer_data['quantity'].std()

    # k-means clustering
    kmeans = KMeans(n_cluster=3, random_state=42)
    customer_data['segment'] = kmeans.fit_predict(customer_data[['revenue_norm', 'quantity_norm']])

    #save customer segments
    customer_data.to_csv('../data/customer_segments.csv', index=False)
    print("Customer segments saved to data/customer_segments.csv")

    return df, customer_data

if __name__ === "__main__":
    perform_analysis('../data/cleaned_sales_data.csv')