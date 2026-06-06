# Mutual Fund Analytics & Risk Intelligence Dashboard

## Project Overview

This project was developed as part of the Bluestock Mutual Fund Analytics Capstone Project. The objective is to analyze mutual fund performance, investor behavior, industry trends, and risk metrics using Python, SQL, SQLite, and Power BI.

The project includes data ingestion, cleaning, exploratory data analysis (EDA), performance analytics, risk analytics, and an interactive Power BI dashboard.

---

## Objectives

* Analyze mutual fund industry trends.
* Evaluate fund performance using risk-adjusted metrics.
* Study investor transaction patterns.
* Build an interactive dashboard for decision-making.
* Generate insights for investors and fund managers.

---

## Technology Stack

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Plotly
* SQLite
* SQLAlchemy
* Power BI
* Git & GitHub

---

## Project Structure

bluestock_mf_capstone/

data/

* raw/
* processed/

notebooks/

* 01_data_ingestion.ipynb
* 02_data_cleaning.ipynb
* 03_eda_analysis.ipynb
* 04_performance_analytics.ipynb
* 05_advanced_analytics.ipynb

scripts/

* live_nav_fetch.py
* etl_pipeline.py
* compute_metrics.py
* recommender.py

sql/

* schema.sql
* queries.sql

dashboard/

* bluestock_mf_dashboard.pbix

reports/

* Dashboard.pdf
* Final_Report.pdf
* Bluestock_MF_Presentation.pptx

---

## Key Features

### Data Engineering

* Data ingestion from CSV files.
* Live NAV fetching using MFAPI.
* Data validation and cleaning.
* SQLite data warehouse implementation.

### Exploratory Data Analysis

* NAV trend analysis.
* AUM growth analysis.
* SIP inflow trends.
* Folio growth analysis.
* Sector allocation analysis.

### Performance Analytics

* CAGR Calculation
* Sharpe Ratio
* Sortino Ratio
* Alpha & Beta
* Maximum Drawdown
* Rolling Sharpe Ratio

### Risk Analytics

* Historical VaR (95%)
* Conditional VaR (CVaR)
* Fund Scorecard
* Benchmark Comparison

### Dashboard Pages

#### Executive Overview

Industry-wide KPIs and trend analysis.

#### Risk Analytics

Sharpe Ratio, Sortino Ratio, VaR, and Maximum Drawdown.

#### Fund Analysis

Fund category and risk category analysis.

#### Investor Analytics

Investor demographics, transaction behavior, and geographic insights.

---

## Key Findings

* Mutual fund folios increased significantly between 2022 and 2025.
* SIP inflows demonstrated steady growth across the analysis period.
* Several funds achieved superior risk-adjusted performance measured by Sharpe and Sortino Ratios.
* Investor participation was concentrated in selected states and city tiers.
* Equity-oriented funds dominated industry inflows and folio growth.

---

## Author

Vaddeyraju Sai Siddartha

---

## License

Academic Project – Bluestock Mutual Fund Analytics Capstone.
