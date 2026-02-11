"""
Command-line menu for the Stock Dashboard application.
"""

from typing import Optional


def start_cli() -> None:
    """
    Entry point for the command-line interface.

    Handles the main menu loop and user interaction.
    """
    print_welcome()

    while True:
        choice = show_main_menu()

        if choice == "1":
            handle_stock_lookup()
        elif choice == "2":
            print("\nExiting Stock Dashboard. Goodbye!\n")
            break
        else:
            print("\nInvalid choice. Please select a valid option.\n")


def print_welcome() -> None:
    """
    Display a welcome message to the user.
    """
    print("\n==============================")
    print("   📈 Stock Dashboard CLI")
    print("==============================\n")


def show_main_menu() -> str:
    """
    Display the main menu and return the user's choice.
    """
    print("Main Menu:")
    print("1. Look up a stock")
    print("2. Exit")

    return input("\nSelect an option (1–2): ").strip()


def handle_stock_lookup() -> None:
    """
    Handle user input for stock lookup.
    """
    user_input = input(
        "\nEnter a stock ticker or company name (e.g., AAPL or Apple): "
    ).strip()

    if not user_input:
        print("\nNo input provided. Returning to main menu.\n")
        return

    # Placeholder for future integration
    print(f"\nYou entered: {user_input}")
    print("(Stock search logic will be added here.)\n")
