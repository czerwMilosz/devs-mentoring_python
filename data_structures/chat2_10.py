# 10. Najdroższy produkt

CART = [
    {"name": "apple", "price": 3, "quantity": 4},
    {"name": "banana", "price": 2, "quantity": 6},
    {"name": "milk", "price": 5, "quantity": 2}
]

def most_expensive_product(cart: list[dict]) -> str:
    max_item = max(cart, key=lambda x: x["price"])
    return max_item["name"]

def main():
    print(most_expensive_product(CART))

if __name__ == "__main__":
    main()