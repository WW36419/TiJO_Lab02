import unittest


class Calc:

    def add(self, num1, num2):
        return float(num1) + float(num2)

    def subtract(self, num1, num2):
        return float(num1) - float(num2)

    def multiply(self, num1, num2):
        return float(num1) * float(num2)

    def divide(self, num1, num2):
        return float(num1) / float(num2)


class TestCalc(unittest.TestCase):

    def setUp(self):
        print("* setUp()")
        self.calc = Calc()

    def test_add(self):
        print("** test_add()")
        # Arrange
        num1 = 3
        num2 = 2
        # Act
        result = self.calc.add(num1, num2)
        # Assert
        self.assertEqual(result, 5)

    def test_subtract(self):
        print("** test_subtract()")
        # Arrange
        num1 = 5
        num2 = 2
        # Act
        result = self.calc.subtract(num1, num2)
        # Assert
        self.assertEqual(result, 3)

    def test_multiply(self):
        print("** test_multiply")
        # Arrange
        num1 = 3
        num2 = 2
        # Act
        result = self.calc.multiply(num1, num2)
        # Assert
        self.assertEqual(result, 6)

    def test_divide(self):
        print("** test_divide")
        # Arrange
        num1 = 9
        num2 = 3
        # Act
        result = self.calc.divide(num1, num2)
        # Assert
        self.assertEqual(result, 3)

    def test_divide_by_zero(self):
        print("** test_divide_by_zero")
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)

    def tearDown(self):
        print("*** tearDown()")
        self.calc = None


if __name__ == "__main__":
    unittest.main()
