class Order:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Order(id={self.id}, name='{self.name}', price={self.price})"


class Manager:
    def __init__(self):
        self.orders = {}

    def add_order(self, order: Order, quantity: int) -> None:
        # for existing_order in self.orders:
        #     if existing_order.id == order.id:
        #         self.orders[existing_order] += quantity
        #         return

        if order in self.orders:
            self.orders[order] += quantity
            return

        self.orders[order] = quantity

    def __str__(self):
        return f"{self.orders}"


def main():
    order = Order(1, "test", 100)
    manager = Manager()

    manager.add_order(order, 1)
    manager.add_order(order, 2)

    print(manager)


if __name__ == "__main__":
    main()