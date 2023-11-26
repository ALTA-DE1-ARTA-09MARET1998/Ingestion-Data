import pandas as pd

parquet_file_path = '/Users/macbookair/Documents/Arter/Data-Engineer-Bootcamp/Technical-Assignment/Ingestion-Data/dataset/yellow_tripdata_2023-01.parquet'

df = pd.read_parquet(parquet_file_path)
df = df.rename(columns=lambda x: x.lower().replace(' ', '_'))
print(df)
df.dropna(inplace=True)

df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])

df = df[df['trip_distance'] <= 100]

print("\nCleaned Dataset Info:")
print(df.info())
df.to_parquet('/Users/macbookair/Documents/Arter/Data-Engineer-Bootcamp/Technical-Assignment/Ingestion-Data/dataset/yellow_tripdata_2023-01.parquet', index=False)

def __create_connection(self):
    from sqlalchemy import create_engine

    user = "postgres"
    password = "admin"
    host = "localhost"
    database = "mydb"
    port = 5432
    conn_string = f"postgresql://{user}:{password}@{host}:{port}/{database}"

    self.engine = create_engine(conn_string)

# database_name = 'yellow_trip'
# table_name = 'yellow_trip'

# engine = create_engine('postgresql:///yellow_trip.db')
# dtype_mapping = {
#     'column1': 'INTEGER',
#     'column2': 'TEXT',
#     'column3': 'REAL',
#     # Add more columns as needed
# }

# df.to_sql(name=table_name, con=engine, if_exists='replace', index=False, dtype=dtype_mapping)
