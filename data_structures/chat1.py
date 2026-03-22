from collections import defaultdict

transactions = [
    ["Tom", "food", 20],
    ["Tom", "transport", 15],
    ["Tom", "food", 10],
    ["Clare", "food", 25],
    ["Clare", "entertainment", 50],
    ["Rich", "transport", 5],
    ["Rich", "food", 30],
]

# OUTPUT
"""{
    "Tom": {
        "actions": ["login", "view", "view", "purchase"],
        "counts": {
            "login": 1,
            "view": 2,
            "purchase": 1
        },
        "has_purchase": True
    },
    ...
}"""



def create_summary():
    return {
        "categories": [],
        "total": 0,
        "by_category": defaultdict(int)
    }

def aggregate_bill_by_person(bill: list[list[str, str, float]]) -> dict:
    summary = defaultdict(create_summary)
    for person, category, price in bill:
        summary[person]["categories"].append(category)
        summary[person]["total"] += price
        summary[person]["by_category"][category] += price
    for person in summary:
        summary[person]["by_category"] = dict(summary[person]["by_category"])

    return dict(summary)

def main():
    summary = aggregate_bill_by_person(transactions)
    print(summary)

if __name__ == "__main__":
    main()