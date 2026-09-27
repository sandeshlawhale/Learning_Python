# learning the polymorphysm and inheritance


class Payment:
    def process_payment(self, amount):
        raise NotImplementedError


class CreditCardPayment(Payment):
    def __init__(self, card_holder_name, card_holder_number):
        self.card_holder_name = card_holder_name
        self.card_holder_number = card_holder_number

    def process_payment(self, amount):
        return f"Paying {amount} via Credit Card with ending number of {self.card_holder_number[-4:]}"


class UPIPayment(Payment):
    def __init__(self, upi_id):
        self.upi_id = upi_id

    def process_payment(self, amount):
        return f"Paying {amount} via {self.upi_id}"


class PayPalPayment(Payment):
    def __init__(self, email):
        self.email = email

    def process_payment(self, amount):
        return f"Paying {amount} via Paypal {self.email}"


payments = [
    CreditCardPayment("jane doe", "1234567887654321"),
    UPIPayment("janedoe@upi"),
    PayPalPayment("jane.doe@gmail.com"),
]

for payment in payments:
    print(payment.process_payment(5000))
