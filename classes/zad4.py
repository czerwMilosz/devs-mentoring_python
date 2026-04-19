class BankAccount:
    def __init__(self, number: int, owner: str, balance:float):
        if balance < 0:
            raise ValueError("Balance cannot be negative")
        self.number = number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        fee = (amount // 100) * 2
        self.balance += amount - fee

    def withdraw(self, amount: float) -> None:
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        if amount > self.balance:
            print("Insufficient funds")
            return
        self.balance -= amount

    def change_ownership(self, new_owner: str) -> None:
        self.owner = new_owner

    def display(self) -> None:
        print(f"Owner: {self.owner}")
        print(f"Number: {self.number}")
        print(f"Balance: {self.balance}")

def main():
    account = BankAccount(1234123, "Adam", 0)
    account.deposit(50)
    account.withdraw(60)
    account.change_ownership("Tomasz")
    account.display()

if __name__ == "__main__":
    main()