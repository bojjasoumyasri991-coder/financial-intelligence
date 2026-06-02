# Financial Intelligence System

## Overview

A Financial Intelligence Platform for Nifty 100 companies.

### Stream A – Power BI Dashboards

1. Executive Market Overview
2. Company Deep Dive
3. Sector Comparison Analyzer
4. Financial Health Scorecard
5. Debt & Leverage Monitor
6. Growth & Valuation Analytics
7. Dividend & Shareholder Returns

### Stream B – Data Engineering

PostgreSQL Star Schema:

- dim_company
- dim_date
- dim_sector

Fact Tables:

- fact_financials
- fact_profit_loss
- fact_balance_sheet
- fact_cash_flow
- fact_documents
- fact_health_scores

Python Analytics:

- Health Scoring Engine
- Anomaly Detection
- Trend Analysis
- Pros & Cons Generator

### Stream C – Django REST API

Endpoint:

GET /api/companies/

Returns company master data from PostgreSQL warehouse.