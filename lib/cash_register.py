#!/usr/bin/env python3
class CashRegister:
    def __init__(self, discount=0,):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = 0

    def add_item(self, title, price=0.98, quantity=1):
        self.title = title
        self.price = price
        self.quantity = quantity
        self.last_transaction = price * quantity
        self.total += self.last_transaction
        for i in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        if self.discount == 20:
            self.total = self.total - (self.total * self.discount /100)
            print(f'After the discount, the total comes to ${int(self.total)}.')
        elif self.discount == 0:
            print('There is no discount to apply.')


    def void_last_transaction(self):
        self.total -= self.last_transaction
