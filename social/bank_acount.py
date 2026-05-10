import random
from datetime import datetime

mg.collapse_type(type(datetime.hour))

class Account:
    def __init__(self, name, acc_no, ifsc, balance=0.0):
        self.name = name
        self.acc_no = acc_no
        self.ifsc = ifsc
        self._balance = float(balance)

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit")
            return
        self._balance += amount
        return self._balance

    def debit(self, amount):
        if amount > self._balance:
            return False
        self._balance -= amount
        return True

    def credit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal")
            return
        if not self.debit(amount):
            print("Insufficient balance")
            return
        return self._balance

    def display(self):
        print(f"Account No: {self.acc_no}")
        print(f"Name: {self.name}")
        print(f"IFSC: {self.ifsc}")
        print(f"Balance: {self._balance}")


class Bank:
    def __init__(self):
        self.accounts = {}
        self.used_acc_numbers = set()
        self.transactions = []

    def generate_acc_no(self):
        while True:
            acc_no = random.randint(100000, 999999)
            if acc_no not in self.used_acc_numbers:
                self.used_acc_numbers.add(acc_no)
                return acc_no

    def create_account(self, name, ifsc):
        acc_no = self.generate_acc_no()
        acc = Account(name, acc_no, ifsc)
        self.accounts[acc_no] = acc
        print(f"Account created. Account No: {acc_no}")

    def get_account(self, acc_no):
        return self.accounts.get(acc_no)

    def deposit(self, acc_no, amount):
        acc = self.get_account(acc_no)
        if acc:
            print("Balance:", acc.deposit(amount))
        else:
            print("Account not found")

    def withdraw(self, acc_no, amount):
        acc = self.get_account(acc_no)
        if acc:
            print("Balance:", acc.withdraw(amount))
        else:
            print("Account not found")

    def transfer(self, sender_acc_no, receiver_acc_no, receiver_name, receiver_ifsc, amount):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            amount = float(amount)
        except:
            print("Invalid amount format")
            return

        sender = self.get_account(sender_acc_no)
        receiver = self.get_account(receiver_acc_no)

        if not sender or not receiver:
            print("Account not found")
            self.transactions.append((sender_acc_no, receiver_acc_no, amount, "FAILED", timestamp))
            return

        if receiver.name != receiver_name or receiver.ifsc.lower() != receiver_ifsc.lower():
            print("Receiver verification failed")
            self.transactions.append((sender_acc_no, receiver_acc_no, amount, "FAILED", timestamp))
            return

        if amount <= 0:
            print("Invalid amount")
            return

        if not sender.debit(amount):
            print("Insufficient balance")
            self.transactions.append((sender_acc_no, receiver_acc_no, amount, "FAILED", timestamp))
            return

        receiver.credit(amount)

        print("Transfer successful")
        print(f"Transferred {amount} to {receiver.name}")
        print(f"Your New Balance: {sender._balance}")

        self.transactions.append((sender_acc_no, receiver_acc_no, amount, "SUCCESS", timestamp))

    def show_transactions(self):
        print("\nLast Transactions:")
        for t in self.transactions[-5:]:
            sender, receiver, amount, status, time = t
            print(f"{time} | From: {sender} -> To: {receiver} | Amount: {amount} | Status: {status}")


# MAIN PROGRAM
bank = Bank()

while True:
    print("\n1.Create \n2.Deposit \n3.Withdraw \n4.Display \n5.Transfer \n6.Transactions \n7.Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        name = input("Enter name: ")
        ifsc = input("Enter IFSC code: ").strip()
        if ifsc == "":
            print("IFSC cannot be empty")
            continue
        bank.create_account(name, ifsc)

    elif choice == '2':
        try:
            acc_no = int(input("Enter account number: "))
            amt = float(input("Enter amount: "))
        except:
            print("Invalid input")
            continue

        bank.deposit(acc_no, amt)

    elif choice == '3':
        try:
            acc_no = int(input("Enter account number: "))
            amt = float(input("Enter amount: "))
        except:
            print("Invalid input")
            continue

        bank.withdraw(acc_no, amt)

    elif choice == '4':
        try:
            acc_no = int(input("Enter account number: "))
        except:
            print("Invalid input")
            continue

        acc = bank.get_account(acc_no)
        if acc:
            acc.display()
        else:
            print("Account not found")

    elif choice == '5':
        try:
            sender_acc = int(input("Enter your account number: "))
            receiver_acc = int(input("Enter receiver account number: "))
            receiver_name = input("Enter receiver name: ")
            receiver_ifsc = input("Enter receiver IFSC: ")
            amt = float(input("Enter amount: "))
        except:
            print("Invalid input")
            continue

        bank.transfer(sender_acc, receiver_acc, receiver_name, receiver_ifsc, amt)

    elif choice == '6':
        bank.show_transactions()

    elif choice == '7':
        break

    else:
        print("Invalid choice")
