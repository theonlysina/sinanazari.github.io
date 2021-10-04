import unittest

from expenses import *

class Expenses_Test(unittest.TestCase):

    def setUp(self):
        """The setUp function runs before every test function."""

        #load expenses file
        self.expenses = import_expenses('expenses.txt')

    def test_import_expenses(self):

        #test existing total expenses
        self.assertAlmostEqual(45, self.expenses['clothes'])
        self.assertAlmostEqual(7.57, self.expenses['coffee'])
        self.assertAlmostEqual(135.62, self.expenses['entertainment'])

    def test_get_expense(self):

        #test getting expenses based on expense type
        self.assertAlmostEqual(7.57, get_expense(self.expenses, "coffee"))
        self.assertAlmostEqual(5, get_expense(self.expenses, "food"))

        # ADDED: edge
        self.assertEqual(None, get_expense(self.expenses, ""))
        self.assertEqual(None, get_expense(self.expenses, "airplane"))


    def test_add_expense(self):

        #test adding a new expense
        add_expense(self.expenses, "fios", 84.5)
        self.assertAlmostEqual(84.5, self.expenses.get("fios"))

        # test adding an existing expense
        add_expense(self.expenses, "coffee", 1)
        self.assertAlmostEqual(8.57, self.expenses.get("coffee"))

        # EDGE: test adding a negative expense amount
        add_expense(self.expenses, "clothes", -1)
        self.assertAlmostEqual(self.expenses.get("coffee"), 7.57)

        # EDGE: test adding a non-number (non-floatable) expense amount
        add_expense(self.expenses, "clothes", "coffee")
        self.assertAlmostEqual(self.expenses.get("clothes"), 45)

    def test_add_expense(self):

        #test adding a new expense
        add_expense(self.expenses, "fios", 84.5)
        self.assertAlmostEqual(84.5, self.expenses.get("fios"))

        # test adding an existing expense
        add_expense(self.expenses, "coffee", 1)
        self.assertAlmostEqual(8.57, self.expenses.get("coffee"))

        # EDGE: test adding a negative expense amount
        add_expense(self.expenses, "clothes", -1)
        self.assertAlmostEqual(self.expenses.get("clothes"), 45)

        # EDGE: test adding a non-number (non-floatable) expense amount
        add_expense(self.expenses, "clothes", "coffee")
        self.assertAlmostEqual(self.expenses.get("clothes"), 45)

    def test_deduct_expense(self):

        # normal test deducting from expense
        deduct_expense(self.expenses, "coffee", .99)
        self.assertAlmostEqual(6.58, self.expenses.get("coffee"))

        # test deducting too large an amount (> current expense amount) from expense
        # should return a runtime error
        self.assertRaises(RuntimeError, deduct_expense, self.expenses, "coffee", 100.00)

        # EDGE: test removing a non-existent expense amount
        deduct_expense(self.expenses, "airplane", .99)
        self.assertEqual(None, self.expenses.get("airplane"))

        # EDGE: test removing a negative expense amount
        deduct_expense(self.expenses, "clothes", -1)
        self.assertAlmostEqual(self.expenses.get("clothes"), 45)

        # EDGE: test adding a non-number (non-float convertible) expense amount
        deduct_expense(self.expenses, "clothes", "coffee")
        self.assertAlmostEqual(self.expenses.get("clothes"), 45)

    def test_update_expense(self):

        #test updating an expense
        update_expense(self.expenses, "clothes", 19.99)
        self.assertAlmostEqual(19.99, get_expense(self.expenses, "clothes"))

        # EDGE: test updating an expense to 0.00
        update_expense(self.expenses, "food", 0.00)
        self.assertAlmostEqual(0.00, get_expense(self.expenses, "food"))

        # EDGE: test updating an expense that does not exist
        update_expense(self.expenses, "skydiving", 799.99)
        self.assertEqual(None, get_expense(self.expenses, "skydiving"))

    def test_sort_expenses(self):

        #test sorting expenses by 'expense_type'
        expense_type_sorted_expenses = [('clothes', 45.0),
                                        ('coffee', 7.57),
                                        ('entertainment', 135.62),
                                        ('food', 5.0),
                                        ('rent', 825.0)]

        self.assertListEqual(expense_type_sorted_expenses, sort_expenses(self.expenses, "expense_type"))

        # ADDED: test sorting expenses by 'amount'
        amount_sorted_expenses = [('rent', 825.0),
                                        ('entertainment', 135.62),
                                        ('clothes', 45.0),
                                        ('coffee', 7.57),
                                        ('food', 5.0)]

        self.assertListEqual(amount_sorted_expenses, sort_expenses(self.expenses, "amount"))


if __name__ == '__main__':
    unittest.main()
