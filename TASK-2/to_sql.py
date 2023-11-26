import pandas as pd
from sqlalchemy import create_engine

parquet_file_path = '/Users/macbookair/Documents/Arter/Data-Engineer-Bootcamp/Technical-Assignment/Ingestion-Data/dataset/yellow_tripdata_2023-01.parquet'

df = pd.read_parquet(parquet_file_path)
df = df.rename(columns=lambda x: x.lower().replace(' ', '_'))
print(df)

database_name = 'yellow_trip'
table_name = 'yellow_trip'

engine = create_engine(f'sqlite:///yellow_trip.db')
dtype_mapping = {
    'column1': 'INTEGER',
    'column2': 'TEXT',
    'column3': 'REAL',
    # Add more columns as needed
}

df.to_sql(name=table_name, con=engine, if_exists='replace', index=False, dtype=dtype_mapping)
