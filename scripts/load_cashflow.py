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

df = pd.read_excel(
    "data/cashflow.xlsx",
    skiprows=1
)

print(df.columns)
print(df.head())

df.to_sql(
    "fact_cash_flow",
    engine,
    schema="warehouse",
    if_exists="append",
    index=False
)

print("Cash Flow Loaded Successfully")