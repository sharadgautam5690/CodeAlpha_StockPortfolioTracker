"""CodeAlpha Internship Task 2: Stock Portfolio Tracker."""
import csv

# Fixed sample prices for this project; these are not live market prices.
STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "GOOGL": 140.00,
    "MSFT": 420.00,
    "AMZN": 175.00,
}


def get_positive_quantity():
    while True:
        try:
            quantity = int(input("Enter quantity: ").strip())
            if quantity > 0:
                return quantity
            print("Quantity must be greater than zero.")
        except ValueError:
            print("Please enter a valid whole number.")


def save_portfolio(portfolio, filename="portfolio_summary.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Stock", "Quantity", "Price per Share", "Investment Value"])
        for item in portfolio:
            writer.writerow([
                item["stock"], item["quantity"],
                f'{item["price"]:.2f}', f'{item["value"]:.2f}'
            ])
        total = sum(item["value"] for item in portfolio)
        writer.writerow([])
        writer.writerow(["", "", "Total Investment", f"{total:.2f}"])


def main():
    portfolio = []
    print("=" * 48)
    print("          STOCK PORTFOLIO TRACKER")
    print("=" * 48)
    print("Available stocks and sample prices (USD):")
    for symbol, price in STOCK_PRICES.items():
        print(f"{symbol}: ${price:.2f}")

    print("\nEnter stocks you own. Type DONE when finished.")
    while True:
        symbol = input("\nEnter stock symbol: ").strip().upper()
        if symbol == "DONE":
            break
        if symbol not in STOCK_PRICES:
            print("Stock not found. Choose a symbol from the list.")
            continue

        quantity = get_positive_quantity()
        price = STOCK_PRICES[symbol]
        value = price * quantity
        portfolio.append({
            "stock": symbol, "quantity": quantity,
            "price": price, "value": value
        })
        print(f"Added {quantity} share(s) of {symbol}: ${value:,.2f}")

    if not portfolio:
        print("\nNo stocks were added. Portfolio not created.")
        return

    print("\n" + "=" * 65)
    print(f'{"STOCK":<12}{"QUANTITY":>10}{"PRICE/SHARE":>18}{"VALUE":>20}')
    print("-" * 65)
    for item in portfolio:
        print(
            f'{item["stock"]:<12}{item["quantity"]:>10}'
            f'${item["price"]:>16,.2f}${item["value"]:>18,.2f}'
        )
    total = sum(item["value"] for item in portfolio)
    print("-" * 65)
    print(f'{"TOTAL INVESTMENT":<40}${total:>24,.2f}')
    print("=" * 65)
    save_portfolio(portfolio)
    print("\nPortfolio saved to portfolio_summary.csv")


if __name__ == "__main__":
    main()
