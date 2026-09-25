class Money:
    def __init__(self, amount, currency="INR"):
        self.amount = float(amount)
        self.currency = currency

    def __add__(self, other):  # + operator
        if self.currency != other.currency:
            raise ValueError("Cannot add different currencies")
        return Money(self.amount + other.amount, self.currency)

    def __sub__(self, other):  # - operator
        if self.currency != other.currency:
            raise ValueError("Cannot subtract different currencies")
        return Money(self.amount - other.amount, self.currency)

    def __eq__(self, other):  # == operator
        return (
            self.amount == other.amount
            and self.currency == other.currency
        )

    def __str__(self):
        return f"{self.amount:,.2f} {self.currency}"


# Usage
inv1 = Money(1000.0)             # Invoice 1: ₹1000
inv2 = Money(2500.5)             # Invoice 2: ₹2500.50
total = inv1 + inv2              # Calls __add__
balance = total - Money(500.0)   # Calls __sub__

print(total)
print(balance)
print(total == Money(3500.5))    # Calls __eq__
