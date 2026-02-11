from src.menu import show_main_menu, get_ticker_input
from src.market_data import fetch_price_history
from src.storage import save_prices


def main():
    choice = show_main_menu()

    if choice == "download":
        ticker = get_ticker_input()

        print(f"Downloading data for {ticker}...")
        prices = fetch_price_history(ticker)

        save_prices(ticker, prices)
        print("Data saved successfully.")

    else:
        print("Goodbye!")


if __name__ == "__main__":
    main()
