ORDERS = {"Klient_1335":
              {"nazwa_potrawy": "rosół",
               "ocena": 5,
               "rachunek": 20.0},
          "Klient_222":
               {"nazwa_deseru": "lody waniliowe",
               "rachunek": 5.0 }}


def print_orders(orders) -> None:
    for client, order in orders.items():
        print(f"\n{client}:")
        for key, value in order.items():
            print(f"{key} {value}")

def main():
    print_orders(ORDERS)

if __name__ == "__main__":
    main()
