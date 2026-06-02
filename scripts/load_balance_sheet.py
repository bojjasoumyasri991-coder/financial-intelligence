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

# Read Excel
df = pd.read_excel(
    "data/balancesheet.xlsx",
    skiprows=1
)

# Clean column names
df.columns = (
    df.columns
      .str.strip()
      .str.lower()
      .str.replace(" ", "_")
)

print(df.columns)
print(df.head())

# Rename company -> company_id
df = df.rename(columns={
    "company": "company_id"
})

df.to_sql(
    "fact_balance_sheet",
    engine,
    schema="warehouse",
    if_exists="append",
    index=False
)

print("Balance Sheet Loaded Successfully")