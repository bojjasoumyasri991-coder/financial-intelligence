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

dates = pd.date_range(
    start="2020-01-01",
    end="2025-12-31",
    freq="D"
)

df = pd.DataFrame()

df["full_date"] = dates
df["year"] = dates.year
df["quarter"] = dates.quarter
df["month"] = dates.month
df["month_name"] = dates.month_name()

df.to_sql(
    "dim_date",
    engine,
    schema="warehouse",
    if_exists="append",
    index=False
)

print("Date Dimension Loaded Successfully")