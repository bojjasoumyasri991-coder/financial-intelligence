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
    "data/documents.xlsx",
    skiprows=1
)

# Rename Excel columns to match PostgreSQL table
df = df.rename(columns={
    "company_id": "company",
    "Year": "year",
    "Annual_Report": "annual_report"
})

print(df.columns)
print(df.head())

df.to_sql(
    "fact_documents",
    engine,
    schema="warehouse",
    if_exists="append",
    index=False
)

print("Documents Loaded Successfully")