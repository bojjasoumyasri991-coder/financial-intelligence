import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL Connection
DB_USER = "postgres"
DB_PASSWORD = "mysql123"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "financial-intelligence"

engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# Read Excel file
df = pd.read_excel("data/raw/companies.xlsx")

# First row contains actual column names
df.columns = df.iloc[0]

# Remove first row
df = df.iloc[1:].reset_index(drop=True)

print("Total Companies:", len(df))
print(df.head())

# Save complete dataset
df.to_sql(
    "dim_company_full",
    engine,
    schema="warehouse",
    if_exists="replace",
    index=False
)

print("All companies loaded successfully!")