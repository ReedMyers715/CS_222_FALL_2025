import unittest
from shoppingCart import ShoppingCart, Item
class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()
    def test_AddItem(self):
        item = Item("Book", 12.99)
        self.cart.AddItem(item)
        self.assertIn(item, self.cart.items)

    def test_RemoveItem(self):
        item = Item("Book", 12.99)
        self.cart.AddItem(item)
        self.cart.RemoveItem(item)

if __name__ == '__main__':
    unittest.main()