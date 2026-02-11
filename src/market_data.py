import sqlite3
from pathlib import Path

DB_PATH = Path("data/stocks.db")


def get_connection():
    """Create and return a SQLite connection."""
    DB_PATH.parent.mkdir(exist_ok=True)
    return sqlite3.connect(DB_PATH)


def init_db():
    """Initialize database tables if they don't exist."""
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticker TEXT NOT NULL,
            date TEXT NOT NULL,
            open REAL,
            high REAL,
            low REAL,
            close REAL,
            volume INTEGER,
            UNIQUE(ticker, date)
        )
        """)

        conn.commit()


def insert_price_data(ticker, rows):
    """
    Insert price rows for a ticker.
    rows = iterable of (date, open, high, low, close, volume)
    """
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.executemany("""
        INSERT OR IGNORE INTO prices
        (ticker, date, open, high, low, close, volume)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, [(ticker, *row) for row in rows])

        conn.commit()


def fetch_prices(ticker, start_date, end_date):
    """Fetch prices for a ticker within a date range."""
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("""
        SELECT date, open, high, low, close, volume
        FROM prices
        WHERE ticker = ?
          AND date BETWEEN ? AND ?
        ORDER BY date
        """, (ticker, start_date, end_date))

        return cursor.fetchall()
