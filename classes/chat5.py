from decimal import Decimal


class Order:
    """Represents a single product order with price and quantity."""

    def __init__(self, product_name: str, price: Decimal, quantity: int):
        """Initializes order with validation for name, price, and quantity."""
        if price <= 0 or quantity <= 0:
            raise ValueError("Price and quantity must be above 0")
        if not product_name.strip():
            raise ValueError("Product name cannot be an empty string")

        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    def __repr__(self) -> str:
        """Returns a developer-friendly string representation of the order."""
        return (
            f"Order(product_name={self.product_name!r}, "
            f"price={self.price}, quantity={self.quantity})"
        )

    def total_price(self) -> Decimal:
        """Calculates total price based on unit price and quantity."""
        return self.price * self.quantity


class Cart:
    """Represents a shopping cart managing multiple orders."""

    def __init__(self) -> None:
        """Initializes an empty list of orders."""
        self.orders = []

    def add_order(self, order: Order) -> None:
        """Adds an order or merges it if product already exists."""
        for o in self.orders:
            if o.product_name.lower() == order.product_name.lower():
                o.quantity += order.quantity
                return
        self.orders.append(order)

    def get_total_value(self) -> Decimal:
        """Calculates total value of all orders in the cart."""
        total_value = Decimal("0.00")
        for order in self.orders:
            total_value += order.total_price()
        return total_value

    def remove_order(self, prod_name: str) -> None:
        """Removes a product from the cart by name."""
        for o in self.orders:
            if prod_name.lower() == o.product_name.lower():
                self.orders.remove(o)
                return
        raise ValueError("Product not found")

    def change_quantity(self, prod_name: str, quantity: int) -> None:
        """Changes quantity of a product by a value."""
        for o in self.orders:
            if prod_name.lower() == o.product_name.lower():
                if quantity < 0 and abs(quantity) > o.quantity:
                    raise ValueError("Quantity exceeded")

                o.quantity += quantity
                if o.quantity == 0:
                    self.orders.remove(o)
                return
        raise ValueError("Product not found")

    def __repr__(self) -> str:
        """Returns a developer-friendly string representation of the cart."""
        return f"Cart(orders={self.orders})"


def main():
    cart = Cart()
    o1 = Order(product_name="IPhone", price=Decimal("2999.99"), quantity=3)
    o2 = Order(product_name="Samsung", price=Decimal("1995.95"), quantity=4)
    o3 = Order(product_name="iPhone", price=Decimal("2999.99"), quantity=4)
    o4 = Order(product_name="Motorola", price=Decimal("996.90"), quantity=2)
    cart.add_order(o1)
    cart.add_order(o2)
    cart.add_order(o3)
    cart.add_order(o4)

    for order in cart.orders:
        print(f"{order.product_name}, {order.price:.2f}, {order.quantity}")
    print(f"Total value: {cart.get_total_value():.2f}")


    cart.remove_order("iphone")
    print("\nAfter remove iphone order")
    for order in cart.orders:
        print(f"{order.product_name}, {order.price:.2f}, {order.quantity}")
    print(f"Total value: {cart.get_total_value():.2f}")

    cart.change_quantity("samsung", -4)
    print("\nAfter update quantity samsung order")
    for order in cart.orders:
        print(f"{order.product_name}, {order.price:.2f}, {order.quantity}")
    print(f"Total value: {cart.get_total_value():.2f}")

if __name__ == "__main__":
    main()
