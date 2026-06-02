import pandas as pd
from sqlalchemy import create_engine

DB_USER = "postgres"
DB_PASSWORD = "mysql123"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "financial-intelligence"

engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

df = pd.read_csv("data/raw/sectors.csv")

df.to_sql(
    "dim_sector",
    engine,
    schema="warehouse",
    if_exists="append",
    index=False
)

print("Sector Dimension Loaded Successfully")