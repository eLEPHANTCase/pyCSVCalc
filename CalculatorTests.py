import unittest

from Calculator import Calculator
from CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_subtraction(self):
        test_data = CsvReader("/Test_Subtraction.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_addition(self):
        test_data = CsvReader("/Test_Addition.csv").data
        for row in test_data:
            result = int(row["Result"])
            self.assertEqual(self.calculator.addition(row["Value 1"], row["Value 2"]), result)

    def test_multiplication(self):
        test_data = CsvReader("/Test_Multiplication.csv").data
        for row in test_data:
            result = int(row["Result"])
            self.assertEqual(self.calculator.multiplication(row["Value 1"], row["Value 2"]), result)

    def test_division(self):
        test_data = CsvReader("/Test_Division.csv").data
        for row in test_data:
            result = float(row["Result"])
            self.assertEqual(self.calculator.division(row["Value 1"], row["Value 2"]), result)

    def test_square(self):
        test_data = CsvReader("/Test_Square.csv").data
        for row in test_data:
            result = float(row["Result"])
            self.assertEqual(self.calculator.square(row["Value 1"]), result)

    def test_square_root(self):
        test_data = CsvReader("/Test_Square_Root.csv")
        for row in test_data:
            result = float(row["Result"])
            self.assertEqual(self.calculator.squareroot(row["Value 1"]), result)


    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)


if __name__ == '__main__':
    unittest.main()