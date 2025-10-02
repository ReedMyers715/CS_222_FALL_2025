class ShoppingCart:
    def __init__(self,):
        self.items = []
    def AddItem(self, item):
        self.items.append(item)

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price