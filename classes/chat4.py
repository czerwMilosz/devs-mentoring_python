from decimal import Decimal


class BankAccount:
    def __init__(self, owner: str, balance: Decimal = Decimal("0.00")) -> None:
        if not owner.strip():
            raise ValueError("Owner cannot be empty")
        if balance < 0:
            raise ValueError("Balance cannot be negative")

        self.owner = owner
        self.balance = balance

    def deposit(self, amount: Decimal) -> None:
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        self.balance += amount

    def withdraw(self, amount: Decimal) -> None:
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def get_balance(self) -> Decimal:
        return self.balance

def main():
    account = BankAccount("Tomasz", Decimal("12.33"))

    print(f"{account.get_balance():.2f}")

    account.deposit(Decimal("2.44"))
    print(f"{account.get_balance():.2f}")

    account.withdraw(Decimal("1.23"))
    print(f"{account.get_balance():.2f}")

if __name__ == "__main__":
    main()