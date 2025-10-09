import pandas as pd
import os, sys, json

def _load_lookup_data(lookup_dir):
    """Load card lookup JSONs and flatten nested fields into a standardized DataFrame."""
    all_lookup_df = []
    for file in os.listdir(lookup_dir):
        if file.endswith(".json"):
            path = os.path.join(lookup_dir, file)
            with open(path, "r") as fil:
                raw = json.load(fil)

            data = raw.get("data", [])
            records = []
            for card in data:
                set_id = card.get("set", {}).get("id", "UNKNOWN")
                set_name = card.get("set", {}).get("name", "UNKNOWN")
                card_number = card.get("number", "0")
                card_name = card.get("name", "UNKNOWN")

                market_value = 0.0
                if "tcgplayer" in card:
                    prices = card["tcgplayer"].get("prices", {})
                    if isinstance(prices, dict):
                        for variant in prices.values():
                            if "market" in variant:
                                market_value = variant["market"]
                                break

                records.append({
                    "card_id": f"{set_id}-{card_number}",
                    "set_id": set_id,
                    "card_number": card_number,
                    "set_name": set_name,
                    "card_name": card_name,
                    "card_market_value": market_value
                })

            if records:
                all_lookup_df.append(pd.DataFrame(records))

    if not all_lookup_df:
        return pd.DataFrame(columns=[
            "card_id", "set_id", "card_number",
            "set_name", "card_name", "card_market_value"
        ])

    lookup_df = pd.concat(all_lookup_df, ignore_index=True)
    return lookup_df


def _load_inventory_data(inventory_dir):
    """Load all CSV inventory files and create standardized DataFrame."""
    inventory_data = []
    for file in os.listdir(inventory_dir):
        if file.endswith(".csv"):
            path = os.path.join(inventory_dir, file)
            df = pd.read_csv(path)

            required_cols = ["card_name", "set_id", "card_number",
                             "binder_name", "page_number", "slot_number"]
            missing_cols = [c for c in required_cols if c not in df.columns]
            if missing_cols:
                print(f"[WARNING] Missing columns in {file}: {missing_cols}")
                continue

            df["card_id"] = df["set_id"].astype(str) + "-" + df["card_number"].astype(str)
            inventory_data.append(df)

    if not inventory_data:
        return pd.DataFrame(columns=[
            "card_id", "card_name", "set_id", "card_number",
            "binder_name", "page_number", "slot_number"
        ])

    inventory_df = pd.concat(inventory_data, ignore_index=True)
    return inventory_df


def update_portfolio(inventory_dir, lookup_dir, output_file):
    """Perform ETL: merge inventory + lookup, clean, and save portfolio CSV."""
    lookup_df = _load_lookup_data(lookup_dir)
    inv_df = _load_inventory_data(inventory_dir)

    merged_df = inv_df.merge(lookup_df, on="card_id", how="left", suffixes=("_inv", "_lookup"))

    merged_df["card_name"] = merged_df["card_name_inv"]
    merged_df["set_id"] = merged_df["set_id_inv"]
    merged_df["card_number"] = merged_df["card_number_inv"]
    merged_df["card_market_value"] = merged_df["card_market_value"].fillna(0.0)
    merged_df["set_name"] = merged_df["set_name"].fillna("NOT_FOUND")

    merged_df["index"] = (
        merged_df["binder_name"].astype(str) + "-" +
        merged_df["page_number"].astype(str) + "-" +
        merged_df["slot_number"].astype(str)
    )

    col_order = [
        "index", "card_id", "card_name", "set_id", "card_number",
        "set_name", "card_market_value",
        "binder_name", "page_number", "slot_number"
    ]
    merged_df = merged_df[col_order]

    merged_df.to_csv(output_file, index=False)

def main():
    """Run ETL with full inventory and lookup data."""
    print("--- Running Full Pipeline ---")
    update_portfolio("./card_inventory/", "./card_set_lookup/", "card_portfolio.csv")

def test():
    """Run ETL with test directories."""
    print("--- Running Test Pipeline (Built-in Test Modes) ---")
    update_portfolio("./card_inventory_test/", "./card_set_lookup_test/", "test_card_portfolio.csv")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].lower() == "main":
        main()
    else:
        print("Running in Test Mode...", file=sys.stderr)
        test()
