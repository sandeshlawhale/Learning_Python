class BankAccount:
    def __init__(self, acc_name, acc_id, balance=0):
        self.acc_holder_name = acc_name
        self.acc_number = acc_id
        self._balance = balance

    def deposit(self, amt):
        if amt > 0:
            self._balance += amt

    def withdraw(self, amt):
        if amt > 0 and amt <= self._balance:
            self._balance -= amt

    @property
    def balance(self):
        return self._balance

    def __str__(self):
        return f"{self.acc_holder_name} has {self.balance} Rs"


account = BankAccount("John", "ACC1001")

account.deposit(5000)
account.withdraw(1500)

print(account.balance)
