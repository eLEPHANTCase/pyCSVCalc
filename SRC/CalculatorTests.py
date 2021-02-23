import unittest

from Calculator import Calculator
from CSVReader import CSVReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_subtraction(self):
        test_data = CSVReader("../CSV_Data/Test_Subtraction.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)
        test_data.clear()
        print('done!')

    def test_addition(self):
        test_data = CSVReader("../CSV_Data/Test_Addition.csv").data
        for row in test_data:
            result = int(row["Result"])
            self.assertEqual(self.calculator.add(row["Value 1"], row["Value 2"]), result)
            self.assertEqual(self.calculator.result, result)
        test_data.clear()

    def test_multiplication(self):
        test_data = CSVReader("../CSV_Data/Test_Multiplication.csv").data
        for row in test_data:
            result = int(row["Result"])
            self.assertEqual(self.calculator.multiply(row["Value 1"], row["Value 2"]), result)
        test_data.clear()

    def test_division(self):
        test_data = CSVReader("../CSV_Data/Test_Division.csv").data
        for row in test_data:
            result = float(row["Result"])
            self.assertEqual(self.calculator.divide(row["Value 1"], row["Value 2"]), result)
        test_data.clear()

    def test_square(self):
        test_data = CSVReader("../CSV_Data/Test_Square.csv").data
        for row in test_data:
            result = float(row["Result"])
            self.assertEqual(self.calculator.square(row["Value 1"]), result)
        test_data.clear()

    def test_square_root(self):
        test_data = CSVReader("../CSV_Data/Test_Square_Root.csv")
        for row in test_data:
            result = float(row["Result"])
            self.assertEqual(self.calculator.squareroot(row["Value 1"]), result)
        test_data.clear()

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)


if __name__ == '__main__':
    unittest.main()