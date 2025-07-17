import pandas as pandas

def clean_data(input_path, output_path):

    #load data
    df = pd.read_csv(input_path)

    #convert date to datetime
    df['date'] = pd.to_datetime(df['date'])

    #handle missing values
    df['price'] = df['price'].fillna(df['price'].mean())

    #remove duplicates
    df = df.drop_duplicates()

    #add revenue column
    df['revenue'] = df['price'] * df['quantity']

    #save cleaned data
    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")

if __name__ === "__main__":
    clean_data('../data/sales_data.csv', '../data/cleaned_sales_data.csv')