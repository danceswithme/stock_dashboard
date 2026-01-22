# Stock Dashboard

## Overview
**Stock Dashboard** is a Python-based project for analyzing and visualizing historical stock data.  
It was built for personal practice and to help a family friend better understand investment performance. 
Users can dynamically adjust timeframe, investment amount, and units to compare performance across assets.

The project emphasizes **clean structure, reusable components, and transparent data workflows**, following common industry conventions.

---

## Features
- Accepts **stock ticker symbols or company names** as user input
- Suggests matching tickers when company names are ambiguous
- Downloads and caches ticker metadata automatically on first run
- Loads and processes historical price data
- Calculates basic return metrics
- Generates simple visualizations
- Modular Python architecture using a `src/` layout

---

## Tech Stack
- Python 3.13
- pandas
- numpy
- matplotlib
- rapidfuzz (for name matching)
- pytest

---

## Project Structure
```
stock_dashboard/
├── src/
│   └── stock_dashboard/
│       ├── __init__.py
│       ├── main.py              # Application entry logic
│       │
│       ├── core/                # Analysis & visualization logic
│       │   ├── __init__.py
│       │   ├── analysis.py
│       │   └── charts.py
│       │
│       ├── data/                # Market data access & storage
│       │   ├── __init__.py
│       │   ├── market_data.py
│       │   ├── storage.py
│       │   ├── ticker_loader.py
│       │   └── ticker_search.py
│       │
│       ├── config/              # App configuration
│       │   ├── __init__.py
│       │   └── settings.py
│       │
│       └── cli/                 # Command-line interface
│           ├── __init__.py
│           └── menu.py
│
├── data/
│   └── tickers.csv              # Auto-downloaded on first run (gitignored)
│
├── notebooks/                   # Exploratory analysis & prototypes
├── tests/
│   └── test_analysis.py
│
├── run.py                       # Thin launcher script
├── requirements.txt
├── .gitignore
└── README.md
```

> The `data/` directory is excluded from version control and is generated at runtime.

---

## Setup
Clone the repository and create a virtual environment:

```bash
git clone https://github.com/danceswithme/stock_dashboard.git
cd stock_dashboard
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt

## Data Handling
Ticker metadata is **automatically downloaded on first run** and cached locally.  
If the data file already exists, the cached version is used.

No API keys are required.

---

## Usage
Run the application:

```bash
python src/main.py
```

You may enter:
- A stock ticker (e.g. AAPL)
- A company name (e.g. Apple)

If multiple matches are found, the application will prompt you to select the correct ticker.

⸻

Disclaimer

This project is for educational and personal use only.
It is not financial advice.
