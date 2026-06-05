import pandas as pd
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://fi_user:0ub6B5k7j3MJQwXJtTOIFoPNuCHqWTAG@dpg-d8h9chsvikkc73f0slu0-a.singapore-postgres.render.com/financial_intelligence_pk28"

engine = create_engine(DATABASE_URL)

# Read Excel
df = pd.read_excel("data/companies.xlsx")

# Use second row as headers
df.columns = df.iloc[0]

# Remove header row from data
df = df.iloc[1:].reset_index(drop=True)

print(df.columns)
print(df.head())

df.to_sql(
    "dim_company_full",
    engine,
    if_exists="replace",
    index=False
)

print("Companies loaded successfully!")