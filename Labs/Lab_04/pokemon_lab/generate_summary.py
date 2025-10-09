import os, sys
import pandas as pd

def generate_summary(portfolio_file):
    if not os.path.exists(portfolio_file):
        print(f"Error: {portfolio_file} not found.", file=sys.stderr)
        sys.exit(1)

    df = pd.read_csv(portfolio_file)
    if df.empty:
        print("Portfolio is empty.")
        return

    total_value = df["card_market_value"].sum()
    most_valuable = df.loc[df["card_market_value"].idxmax()]

    print(f"Total Portfolio Value: ${total_value:,.2f}")
    print(f"Most Valuable Card: {most_valuable['card_name']} ({most_valuable['card_id']}) - ${most_valuable['card_market_value']:,.2f}")

def main():
    generate_summary("card_portfolio.csv")

def test():
    generate_summary("test_card_portfolio.csv")

if __name__ == "__main__":
    test()