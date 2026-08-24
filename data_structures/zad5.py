BILL_ITEMS = [
    ['Tom', 'Calamari', 6.00],
    ['Tom', 'American Hot', 11.50],
    ['Tom', 'Chocolate Fudge Cake', 4.45],
    ['Clare', 'Bruschetta Originale', 5.35],
    ['Clare', 'Fiorentina', 10.65],
    ['Clare', 'Tiramisu', 4.90],
    ['Rich', 'Bruschetta Originale', 5.35],
    ['Rich', 'La Reine', 10.65],
    ['Rich', 'Honeycomb Cream Slice', 4.90],
    ['Rosie', 'Garlic Bread', 4.35],
    ['Rosie', 'Veneziana', 9.40],
    ['Rosie', 'Tiramisu', 4.90],
]

def aggregate_bill_by_person(bill: list[list[str, str, float]]) -> dict[str, dict[str, any]]:
    summary = {}
    for transaction in bill:
        person, food, price = transaction
        if person not in summary:
            summary[person] = {
                "foods": [food],
                "total": price
            }
        else:
            summary[person]["foods"].append(food)
            summary[person]["total"] += price
    return summary


def main():
    summary = aggregate_bill_by_person(BILL_ITEMS)
    for person, element in summary.items():
        print(f"\n{person}:")
        for category, value in element.items():
            print(f"{category}: {value}")


if __name__ == "__main__":
    main()



