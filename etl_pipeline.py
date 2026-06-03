print("ETL Pipeline Started")
import sqlite3
import pandas as pd

conn = sqlite3.connect("database/mutual_fund.db")

# Load CSV files
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")
aum = pd.read_csv("data/raw/03_aum_by_fund_house.csv")
sip = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")
transactions = pd.read_csv("data/raw/08_investor_transactions.csv")

# Load into SQLite
fund_master.to_sql("dim_fund", conn, if_exists="replace", index=False)
nav_history.to_sql("fact_nav", conn, if_exists="replace", index=False)
aum.to_sql("fact_aum", conn, if_exists="replace", index=False)
sip.to_sql("fact_sip", conn, if_exists="replace", index=False)
transactions.to_sql("fact_transactions", conn, if_exists="replace", index=False)

print("All datasets loaded successfully!")

conn.close()
print("All datasets loaded successfully!")
