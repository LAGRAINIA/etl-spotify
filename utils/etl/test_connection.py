import pandas as pd
from sqlalchemy import create_engine

# Define the connection string
connection_string = 'postgresql://anass:1412@localhost:5432/spotify_data'

# Create an SQLAlchemy engine
engine = create_engine(connection_string)

# Query the database
df = pd.read_sql_query('SELECT * FROM my_table', engine)

print(df)
