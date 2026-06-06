# Mutual Fund Analytics & Risk Intelligence Dashboard

## Executive Summary

The Mutual Fund Analytics & Risk Intelligence Dashboard is an end-to-end data analytics project designed to evaluate mutual fund performance, investor behavior, industry trends, and risk-adjusted returns. The project integrates data engineering, exploratory data analysis, financial risk analytics, database management, and business intelligence reporting into a unified analytics platform.

Using Python, SQLite, SQL, and Power BI, the project transforms raw mutual fund datasets into actionable insights for investors, fund managers, and financial analysts.

---

## Business Problem

The Indian mutual fund industry has witnessed significant growth in assets under management (AUM), investor participation, and systematic investment plans (SIPs). However, investors often struggle to evaluate funds using comprehensive risk-adjusted metrics and industry trends.

This project addresses that challenge by providing:

* Performance evaluation of mutual funds.
* Risk analytics using industry-standard metrics.
* Investor demographic and transaction analysis.
* Interactive dashboard-based decision support.

---

## Project Objectives

* Build a robust ETL pipeline for mutual fund datasets.
* Clean, validate, and store data using SQLite.
* Perform exploratory data analysis to identify trends.
* Calculate advanced performance and risk metrics.
* Develop an interactive Power BI dashboard.
* Generate actionable insights from investor and fund data.

---

## Technology Stack

| Category        | Tools & Technologies        |
| --------------- | --------------------------- |
| Programming     | Python                      |
| Data Analysis   | Pandas, NumPy               |
| Visualization   | Matplotlib, Seaborn, Plotly |
| Database        | SQLite                      |
| ORM             | SQLAlchemy                  |
| Dashboarding    | Power BI                    |
| Version Control | Git, GitHub                 |

---

## Project Architecture

Data Sources → Data Ingestion → Data Cleaning → SQLite Database → Analytics Engine → Power BI Dashboard → Business Insights

---

## Project Workflow

### Phase 1: Data Ingestion

* Imported multiple mutual fund datasets.
* Integrated live NAV data using MFAPI.
* Performed initial data validation and profiling.

### Phase 2: Data Engineering

* Cleaned missing and inconsistent records.
* Standardized formats and business rules.
* Designed a star-schema-inspired SQLite database.

### Phase 3: Exploratory Data Analysis

* NAV trend analysis.
* SIP inflow analysis.
* AUM growth analysis.
* Folio growth analysis.
* Category and sector analysis.

### Phase 4: Performance & Risk Analytics

* CAGR Analysis
* Sharpe Ratio
* Sortino Ratio
* Alpha & Beta
* Maximum Drawdown
* Historical VaR (95%)
* Conditional VaR (CVaR)
* Rolling Sharpe Ratio

### Phase 5: Business Intelligence Dashboard

* Executive Overview
* Risk Analytics
* Fund Analysis
* Investor Analytics

---

## Dashboard Overview

### Executive Overview

Provides industry-level KPIs including:

* Total AUM
* Total SIP Inflows
* Total Schemes
* Total Folios
* AUM Trends

### Risk Analytics

Provides:

* Sharpe Ratio Analysis
* Sortino Ratio Analysis
* Value at Risk (95%)
* Maximum Drawdown Analysis

### Fund Analysis

Provides:

* Category Distribution
* Risk Category Distribution
* Fund House Analysis
* Sub-Category Analysis

### Investor Analytics

Provides:

* State-wise Investment Analysis
* Gender Distribution
* Age Group Analysis
* Transaction Type Analysis
* Monthly Transaction Trends

---

## Key Insights

* SIP inflows demonstrated strong growth throughout the analysis period.
* Equity-oriented funds dominated industry participation.
* Risk-adjusted performance varied significantly across schemes.
* Investor participation was concentrated within key states and urban centers.
* Several funds achieved superior Sharpe and Sortino ratios, indicating strong risk-adjusted returns.

---

## Repository Structure

bluestock_mf_capstone/

├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda_analysis.ipynb
│   ├── 04_performance_analytics.ipynb
│   └── 05_advanced_analytics.ipynb
│
├── scripts/
│   ├── etl_pipeline.py
│   ├── live_nav_fetch.py
│   ├── compute_metrics.py
│   └── recommender.py
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── dashboard/
│   └── bluestock_mf_dashboard.pbix
│
├── reports/
│   ├── Dashboard.pdf
│   ├── Final_Report.pdf
│   └── Bluestock_MF_Presentation.pptx
│
└── README.md

---

## Future Enhancements

* Automated NAV data refresh.
* Streamlit web application deployment.
* Portfolio optimization using Modern Portfolio Theory.
* Monte Carlo simulations for fund forecasting.
* Automated reporting and alerting framework.

---

## Author

**Vaddeyraju Sai Siddartha**

Mutual Fund Analytics & Risk Intelligence Dashboard Project

---

## License

This project was developed for academic and portfolio purposes.
