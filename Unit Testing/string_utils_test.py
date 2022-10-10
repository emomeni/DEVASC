import unittest
import string_utils as s

class TestStringUtils(unittest.TestCase):
    def test_capitalize(self):
        expected = "Cheese"
        actual = s.capitalize("cheese")
        self.assertEqual(actual, expected)
    
    def test_title_case(self):
        expected = "Network Python"
        actual = s.title_case("network python")
        self.assertEqual(actual, expected)



if __name__ == '__main__':
    unittest.main()
