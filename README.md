# EV Population Analysis

An end-to-end data analytics project exploring Washington State's Electric Vehicle Population dataset — from raw data cleaning in Python, through business-style SQL queries in PostgreSQL, to an interactive Power BI dashboard.

## Overview

This project analyzes ~290,000 electric vehicle registration records to answer questions like:
- Where are EVs most concentrated geographically?
- How has EV adoption grown over time?
- How does electric range vary by manufacturer?
- What share of vehicles are fully electric (BEV) vs plug-in hybrid (PHEV)?

## Tech stack

- **Python** — pandas, matplotlib, seaborn, scipy (cleaning, EDA, statistical testing)
- **PostgreSQL** — business-style SQL queries (via SQLAlchemy for loading)
- **Power BI** — interactive dashboard

## Project structure

```
ev-population-analysis/
├── dashboard/
│   └── power-bi/
│       ├── ev_dashboard.pbix
│       └── screenshot.png
├── data/
│   ├── raw/              # original dataset (not tracked in git)
│   └── cleaned/          # cleaned CSV output from Phase 1
├── src/
│   ├── config.py         # shared file paths
│   ├── 01_load_explore.py
│   ├── 02_eda.py
│   └── 03_load_to_sql.py
├── sql/
│   ├── 01_top_counties.sql
│   ├── 02_bev_vs_phev.sql
│   ├── 03_avg_range_by_make.sql
│   └── 04_growth_by_year.sql
├── reports/
│   └── figures/          # saved chart images
└── README.md
```

## Phase 1 — Data cleaning & EDA (Python)

- Loaded the raw dataset, checked for duplicates and missing values
- Standardized column names (lowercase, underscores)
- Saved a cleaned dataset to `data/cleaned/`
- Explored the data across five angles: top makes, adoption trend by year, electric range distribution, BEV vs PHEV split, and geographic concentration by county

**Key finding:** electric range shows a moderate negative correlation with model year (r = -0.55, p < 0.001). This is likely driven by a growing share of PHEVs (which have shorter electric-only range) in recent registrations, rather than a decline in BEV performance.

## Phase 2 — SQL (PostgreSQL)

Cleaned data was loaded into a local PostgreSQL database and queried with four business-style questions (see `sql/`):

1. **Top counties by EV count** — King County leads by a wide margin (140,130 vehicles), more than 3.8x the next county (Snohomish, 36,508)
2. **BEV vs PHEV breakdown** — 233,544 BEV (80.7%) vs 56,020 PHEV (19.3%)
3. **Average electric range by make** — filtered to manufacturers with 100+ vehicles to avoid low-sample distortion; Tesla leads in volume (118,148 vehicles) with a 49.1 mile average
4. **Registrations by model year** — confirms the adoption trend seen in Python, peaking in 2023 (60,332 vehicles)

**Note:** the dataset includes 249 distinct counties, not just Washington's 39 — a small number of vehicles were registered outside WA.

## Phase 3 — Power BI dashboard

An interactive dashboard (dark theme with lime green accents) featuring:
- KPI cards: Total EVs, Counties, Avg range, BEV share
- Top 10 counties by EV count (bar chart)
- BEV vs PHEV split (donut chart)
- Registrations by model year (line chart)
- Average range by make (column chart)
- A State slicer for interactive filtering

![EV population dashboard](dashboard/power-bi/screenshot.png)

## Key insights

- **Adoption is accelerating sharply**, especially post-2018, peaking in 2023. The apparent decline after 2023 reflects incomplete registration data for recent years, not an actual drop in adoption.
- **EV ownership is heavily concentrated** around the Seattle metro area (King County).
- **BEVs dominate the market** at roughly 4-to-1 over PHEVs.
- **Electric range varies significantly by manufacturer and sample size** — filtering to high-volume makes gives a more reliable picture than raw averages.

## Data source

Washington State Department of Licensing — Electric Vehicle Population Data.

## Author

Salahddine Dkaki — [GitHub](https://github.com/SALAHDDINEDKAKI) · [LinkedIn](https://www.linkedin.com/in/salahddinedkaki/)
