# 9. Wartość koszyka

CART = [
    {"name": "apple", "price": 3, "quantity": 4},
    {"name": "banana", "price": 2, "quantity": 6},
    {"name": "milk", "price": 5, "quantity": 2}
]

def total_cart_value(cart: list[dict]) -> int:
    return sum(item["price"] * item["quantity"] for item in cart)

def main():
    print(total_cart_value(CART))

if __name__ == "__main__":
    main()