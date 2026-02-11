def main_menu():
    print("\n=== Stock Dashboard ===")
    print("1. Add stock data")
    print("2. View stock data")
    print("3. Exit")

    return input("Select an option: ").strip()


def prompt_stock_inputs():
    ticker = input("Enter stock ticker (e.g. AAPL): ").upper()
    start_date = input("Start date (YYYY-MM-DD): ")
    end_date = input("End date (YYYY-MM-DD): ")
    return ticker, start_date, end_date
