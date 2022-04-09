class Item:
    # Implement the Item here
    def __init__(self , name , price):
        self.name = name
        self.price = price


class ShoppingCart:
    # Implement the ShoppingCart here
    def __init__(self):
        self.items = []

    def add(self , item):
        self.items.append(item)

    def total(self):
        total = 0
        for _ in self.items:
            total += _.price
        return total

    def __len__(self):
        return len(self.items)


item = Item("laptop" , 1000)
print(item.name)

cart = ShoppingCart()
cart.add(item)
print(len(cart))
print(cart.total())

