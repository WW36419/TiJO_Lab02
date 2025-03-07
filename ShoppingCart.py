import unittest


class ShoppingCart:

    def __init__(self):
        self.cart = []
        self.discounts = [
            ['Makaron 500g', 2, "MAK2"]
        ]
        self.active_discounts = []

    def add_product(self, product_name: str, price: int, quantity: int) -> bool:
        """Dodawanie produktu do koszyka"""
        self.cart.append([product_name, price, quantity])
        return True

    def remove_product(self, product_name: str) -> bool:
        """Usuwanie produktu zkoszyka"""
        products = self.get_products()
        idx = products.index(product_name)
        if idx is not None:
            self.cart.pop(idx)
            return True
        else:
            return False

    def update_quantity(self, product_name: str, new_quantity: int) -> bool:
        """Aktualizacja ilości produktu w koszyku"""
        products = self.get_products()
        idx = products.index(product_name)
        if idx is not None:
            self.cart[idx][2] = new_quantity
            return True
        else:
            return False

    def get_products(self):
        """Pobieranie nazw produktów z koszyka"""
        return [product[0] for product in self.cart]

    def count_products(self) -> int:
        """Pobieranie liczby produktów znajdujących się w koszyku"""
        return len(self.cart)

    def get_total_price(self) -> int:
        """Pobieranie sumy cen produktów w koszyku"""
        prices = []
        for product in self.cart:
            price = product[1]
            for discount in self.active_discounts:
                if product[0] == discount[0]:
                    price -= discount[1]
            prices.append(price * product[2])
        return sum(prices)

    def apply_discount_code(self, discount_code: str) -> bool:
        """Zastosowanie kuponu rabatowego"""
        for discount in self.discounts:
            if discount_code == discount[2]:
                self.active_discounts.append([discount[0], discount[1]])
                return True
        return False

    def checkout(self) -> bool:
        """Realizacja zamówienia"""
        print("Zapłacono", self.get_total_price(), "zł")
        self.cart = []
        self.active_discounts = []
        return True


class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        print("* setUp()")
        self.cart = ShoppingCart()

    def test_add_product_should_add_product_to_list(self):
        print("** test_add_product_should_add_product_to_list()")
        # Arrange
        prod1 = ["Woda 1,5L", 2, 2]
        prod2 = ["Chleb 500g", 5, 1]
        # Act
        self.cart.add_product(prod1[0], prod1[1], prod1[2])
        self.cart.add_product(prod2[0], prod2[1], prod2[2])
        results = self.cart.get_products()
        self.cart.checkout()
        # Assert
        self.assertEqual(results[0], "Woda 1,5L")
        self.assertEqual(results[1], "Chleb 500g")
        with self.assertRaises(TypeError):
            self.cart.add_product("Woda 1,5L", None, None)
            self.cart.checkout()

    def test_remove_product_should_remove_product_from_list(self):
        print("** test_remove_product_should_remove_product_from_list")
        # Arrange
        prod1 = ["Woda 1,5L", 2, 2]
        prod2 = ["Chleb 500g", 5, 1]
        prod3 = ["Makaron 500g", 4, 2]
        # Act
        self.cart.add_product(prod1[0], prod1[1], prod1[2])
        self.cart.add_product(prod2[0], prod2[1], prod2[2])
        self.cart.add_product(prod3[0], prod3[1], prod3[2])
        self.cart.remove_product("Chleb 500g")
        res_count = self.cart.count_products()
        res_price = self.cart.get_total_price()
        self.cart.checkout()
        # Assert
        self.assertEqual(res_count, 2)
        self.assertEqual(res_price, 12)
        with self.assertRaises(ValueError):
            self.cart.remove_product("")

    def test_update_quantity_should_change_quantity_of_the_product(self):
        print("** test_update_quantity_should_change_quantity_of_the_product")
        # Arrange
        prod1 = ["Woda 1,5L", 2, 2]
        prod2 = ["Chleb 500g", 5, 1]
        prod3 = ["Makaron 500g", 4, 2]
        # Act
        self.cart.add_product(prod1[0], prod1[1], prod1[2])
        self.cart.add_product(prod2[0], prod2[1], prod2[2])
        self.cart.add_product(prod3[0], prod3[1], prod3[2])
        self.cart.apply_discount_code("MAK2")
        self.cart.update_quantity("Makaron 500g", 3)
        res_price = self.cart.get_total_price()
        self.cart.checkout()
        # Assert
        self.assertEqual(res_price, 15)
        self.assertFalse(self.cart.apply_discount_code("WODA1"))
        with self.assertRaises(ValueError):
            self.cart.update_quantity("Chleb 500g", 3)

    def tearDown(self):
        print("*** tearDown()")
        self.cart = None


if __name__ == "__main__":
    unittest.main()
