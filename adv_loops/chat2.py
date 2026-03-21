TRANSACTIONS = [
    ("food", 20),
    ("transport", 15),
    ("food", 10),
    ("entertainment", 50),
    ("transport", 5)
]

def sum_by_category(transactions: list[tuple[str, int]]) -> dict:
    total = {}
    for category, amount in transactions:
        total[category] = total.get(category,0) + amount
    return total

def main():
    total = sum_by_category(TRANSACTIONS)
    for category, total_amount in total.items():
        print(f"{category}: {total_amount}")

if __name__ == "__main__":
    main()