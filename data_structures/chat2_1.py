# 1. Sumowanie wydatków po kategorii

TRANSACTIONS = [
    ("food", 20),
    ("transport", 15),
    ("food", 10),
    ("entertainment", 50),
    ("transport", 5)
]
def sum_by_category(transactions: list[tuple[str, int]]) -> dict[str, int]:
    """Aggregates transaction amounts by category."""
    totals_by_category = {}
    for category, amount in transactions:
        totals_by_category[category] = totals_by_category.get(category, 0) + amount
    return totals_by_category

def main():
    total_by_category = sum_by_category(TRANSACTIONS)
    for category, amount in total_by_category.items():
        print(f"{category}: {amount}")

if __name__ == "__main__":
    main()