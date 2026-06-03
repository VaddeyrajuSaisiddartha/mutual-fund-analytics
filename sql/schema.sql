CREATE TABLE dim_fund (
    scheme_code INTEGER PRIMARY KEY,
    scheme_name TEXT,
    fund_house TEXT,
    category TEXT,
    sub_category TEXT,
    risk_category TEXT
);

CREATE TABLE fact_nav (
    nav_id INTEGER PRIMARY KEY AUTOINCREMENT,
    scheme_code INTEGER,
    nav_date DATE,
    nav_value REAL
);

CREATE TABLE fact_aum (
    aum_id INTEGER PRIMARY KEY AUTOINCREMENT,
    fund_house TEXT,
    quarter_date TEXT,
    aum_crore REAL
);

CREATE TABLE fact_sip (
    sip_id INTEGER PRIMARY KEY AUTOINCREMENT,
    month_year TEXT,
    sip_inflow REAL,
    active_accounts REAL
);

CREATE TABLE dim_investor (
    investor_id INTEGER PRIMARY KEY,
    age INTEGER,
    state TEXT,
    income_group TEXT,
    city_tier TEXT
);

CREATE TABLE fact_transactions (
    txn_id INTEGER PRIMARY KEY,
    investor_id INTEGER,
    scheme_code INTEGER,
    transaction_type TEXT,
    amount REAL,
    transaction_date DATE
);