import pandas as pd

csv_file_path = '/Users/macbookair/Documents/Arter/Data-Engineer-Bootcamp/Technical-Assignment/Ingestion-Data/dataset/yellow_tripdata_2020-07.csv'
df = pd.read_csv(csv_file_path)
df = df.rename(columns=lambda x: x.lower().replace(' ', '_'))

top_10_passenger_count = df.nlargest(10, 'passenger_count')

# Select specific columns
selected_columns = [
    'vendorid', 'passenger_count', 'trip_distance', 'payment_type',
    'fare_amount', 'extra', 'mta_tax', 'tip_amount', 'tolls_amount',
    'improvement_surcharge', 'total_amount', 'congestion_surcharge'
]

# Display the selected columns for the top 10 rows
result = top_10_passenger_count.loc[:, selected_columns]
print(result)
