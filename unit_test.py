import unittest
import string_manipulation

class TestStringManipulation(unittest.TestCase):

    def setUp(self):
        self.manipulation = string_manipulation.StringManipulation()
    
    def test_change_case(self):
        result = self.manipulation.change_case("Hello World")
        self.assertEqual(result, "HELLO WORLD")
    
    def test_to_alternate_lower(self):
        result = self.manipulation.to_alternate_lower("Hello World")
        self.assertEqual(result, "hElLo wOrLd")
    
    def test_to_csv(self):
        result = self.manipulation.to_csv("Hello World", "string.csv")
        self.assertEqual(result, "CSV created!")



if __name__ == "__main__":
    unittest.main()        