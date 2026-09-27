class Product:
    def __init__(self, name, price, quantity):
        if price > 0:
            self.name = name
            self.price = price
            self.quantity = quantity

    def reduce_quantity(self, q=1):
        if q <= self.quantity:
            self.quantity -= q

    def increase_quantity(self, q=1):
        self.quantity += q

    def __str__(self):
        return f"{self.name} {self.price} {self.quantity}"


class ShoppingCart:
    def __init__(self):
        self.cart = {}
        self._discount = 0

    def add_product(self, name, quantity):
        if name.quantity >= quantity:
            self.cart[name] = self.cart.get(name, 0) + quantity
            name.reduce_quantity(quantity)

    def remove_product(self, name):
        if name in self.cart:
            quantity = self.cart[name]
            del self.cart[name]
            name.increase_quantity(quantity)

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, dis):
        if 0 <= dis <= 100:  # added discount validation
            self._discount = dis  # i was calling 'self.discount' that was making repetative call for the same fun, but then i renamed with underscore for the internal value

    @property
    def total(self):
        price_total = 0
        for n, q in self.cart.items():
            price_total += n.price * q

        discounted_price = price_total - (self._discount / 100) * price_total
        return discounted_price

    def __str__(self):
        print("\nshopping cart:")
        for n, q in self.cart.items():  # use dict.items()
            print(f"{n.name} = {q} * {n.price}")
        print(f"total: {self.total}")
        return ""


laptop = Product("laptop", 75000, 5)
mobile = Product("mobile", 15000, 10)

print(laptop)
print(mobile)

cart = ShoppingCart()
cart.add_product(laptop, 2)
cart.add_product(mobile, 5)

print(cart)

cart.discount = 100
print(cart.total)
