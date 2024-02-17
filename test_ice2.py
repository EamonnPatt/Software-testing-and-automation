# find the minimum number of the input as a list without using sort or min
### This is the second iteration of this and includes the unit test and I have removed the input portion to
#make the unit test work
# all the other test cases like empty list
# Eamonn Patterson
# 1/16/2024
#
###########
import unittest





#find minimum from list function
def find_minimum(values):
    if not values:
        raise ValueError("List is empty. Cannot determine minimum of an empty list.")

    min_value = values[0]
    for value in values:
        if float(value) < min_value:
            min_value = value

    for value in values:
        if not isinstance(value, int):
            raise TypeError("input list can contain only integers.")
    return min_value

 # Test cases in a class so the untit tester can properly see and access them
class TestMinimumFinder(unittest.TestCase):
    def test_short_list(self):
        # Test Case 1
        self.assertEqual(find_minimum([90]), 90)
        self.assertEqual(find_minimum([12, 10]), 10)
        self.assertEqual(find_minimum([10, 12]), 10)
        self.assertEqual(find_minimum([12, 14, 36]), 12)
        self.assertEqual(find_minimum([36, 14, 12]), 12)
        self.assertEqual(find_minimum([14, 12, 36]), 12)

    print('test short list == passed')

    def test_empty_list(self):
        # Test Case 2
        with self.assertRaises(ValueError):
            find_minimum([])
        print('test empty list == passed')

    def test_minimum_is_first_or_last(self):
        # Test Case 3
        self.assertEqual(find_minimum([10, 23, 34, 81, 97]), 10)
        self.assertEqual(find_minimum([97, 81, 34, 23, 10]), 10)
        print('test minimum firt or last == passed')

    def test_negative_elements(self):
        # Test Case 4
        self.assertEqual(find_minimum([10, -2, 5, 23]), -2)
        self.assertEqual(find_minimum([10, -2, -24, 4]), -24)

    def test_case5_elements(self):
        # Test Case 5
        self.assertEqual(find_minimum([-23, -31, -45, -56]), -56)
        self.assertEqual(find_minimum([-6, -203, -2, -78]), -203)
        print('test negative element == passed')

    def test_real_numbers(self):
         #Test Case 6
        with self.assertRaises(TypeError):
            find_minimum([23, 34.56, 67, 33])
        print('test real numbers == passed')

    def test_alphanumeric_elements(self):
        # Test Case 7
        with self.assertRaises(ValueError):
            find_minimum([23, 'hi', 32, 1])
        with self.assertRaises(ValueError):
            find_minimum([12, '&', '*', '34m', '!'])
        print('test alphanumeric == passed')

    def test_duplicate_elements(self):
        # Test Case 8
        self.assertEqual(find_minimum([3, 4, 6, 9, 6]), 3)
        self.assertEqual(find_minimum([13, 6, 6, 9, 15]), 6)
    print('test duplicate == passed')

    def test_large_integer(self):
        # Test Case 9
        self.assertEqual(find_minimum([530, 429449672, 97, 23, 46, 59]), 23)
    print('test large int == passed')

#calls the unit test
if __name__ == "__main__":
    unittest.main()

