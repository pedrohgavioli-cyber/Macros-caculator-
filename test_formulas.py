import unittest
import formulas

class TestFormulas(unittest.TestCase):
    def test_tbm_valid_input(self):
        # Should not raise any errors
        result = formulas.tbm('m', 30, 70, 170)
        self.assertIsNotNone(result)

    def test_tbm_invalid_height(self):
        with self.assertRaises(ValueError) as context:
            formulas.tbm('m', 30, 70, 0)
        self.assertEqual(str(context.exception), "Height must be greater than zero")

        with self.assertRaises(ValueError) as context:
            formulas.tbm('m', 30, 70, -10)
        self.assertEqual(str(context.exception), "Height must be greater than zero")

    def test_tbm_invalid_weight(self):
        with self.assertRaises(ValueError) as context:
            formulas.tbm('m', 30, 0, 170)
        self.assertEqual(str(context.exception), "Weight must be greater than zero")

    def test_tbm_invalid_age(self):
        with self.assertRaises(ValueError) as context:
            formulas.tbm('m', 0, 70, 170)
        self.assertEqual(str(context.exception), "Age must be greater than zero")

if __name__ == '__main__':
    unittest.main()
